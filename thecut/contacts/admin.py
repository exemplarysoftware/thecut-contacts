# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.db import models
from django.forms import TextInput
from thecut.contacts import forms
from thecut.contacts.models import (ContactAddress, ContactGroup, ContactEmail,
    ContactInstantMessengerHandle, ContactNickname, ContactPhone, Organisation,
    Person, PersonOrganisation, ContactWebsite)


def email(obj):
    email = obj.emails.get_first()
    return email and '<a href="mailto:%(email)s" ' \
        'title="%(title)s">%(email)s</a>' %(
        {'email': email, 'title': email.name}) or ''
email.allow_tags = True


def location(obj):
    address = obj.addresses.get_first()
    city = address and address.city or ''
    country = address and address.country or ''
    
    if city and country:
        return '%s, %s' %(city, country)
    else:
        return city or country or ''


def phone(obj):
    phone = obj.phones.get_first()
    return phone or ''


def preview_image(obj):
    html = u''
    try:
        from sorl.thumbnail import get_thumbnail
    except ImportError:
        pass
    else:
        if obj.image:
            try:
                thumb = get_thumbnail(obj.image, '100x75', crop='center')
            except:
                pass
            else:
                html = u'<img src="%s" alt="%s" />' %(thumb.url, str(obj))
    return html
preview_image.short_description = 'Image'
preview_image.allow_tags = True


class ContactAddressInline(admin.StackedInline):
    extra = 0
    fieldsets = [(None, {'fields': ['name', ('street', 'city'),
        ('state', 'postcode'), 'country']})]
    form = forms.ContactAddressInlineForm
    model = ContactAddress
    verbose_name = 'address'
    verbose_name_plural = 'addresses'


class ContactEmailInline(admin.TabularInline):
    extra = 0
    fields = ['name', 'value']
    form = forms.ContactEmailInlineForm
    model = ContactEmail
    verbose_name = 'email address'
    verbose_name_plural = 'email addresses'


class ContactInstantMessengerHandleInline(admin.TabularInline):
    extra = 0
    fields = ['name', 'value', 'type']
    form = forms.ContactInstantMessengerHandleInlineForm
    model = ContactInstantMessengerHandle
    verbose_name = 'instant messenger handle'
    verbose_name_plural = 'instant messenger handles'


class ContactNicknameInline(admin.TabularInline):
    extra = 0
    fields = ['value']
    form = forms.ContactNicknameInlineForm
    model = ContactNickname
    verbose_name = 'nickname'
    verbose_name_plural = 'nicknames'


class ContactPhoneInline(admin.TabularInline):
    extra = 0
    fields = ['name', 'value', 'type']
    form = forms.ContactPhoneInlineForm
    model = ContactPhone
    verbose_name = 'phone number'
    verbose_name_plural = 'phone numbers'


class ContactWebsiteInline(admin.TabularInline):
    extra = 0
    fields = ['name', 'value']
    form = forms.ContactWebsiteInlineForm
    model = ContactWebsite
    verbose_name = 'website'
    verbose_name_plural = 'websites'


class PersonOrganisationInline(admin.TabularInline):
    extra = 0
    model = PersonOrganisation
    verbose_name = 'Organisation'
    verbose_name_plural = 'Organisations'


class OrganisationPersonInline(admin.TabularInline):
    extra = 0
    model = PersonOrganisation
    verbose_name = 'Person'
    verbose_name_plural = 'People'


class CreatedUpdatedMixin(object):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super(CreatedUpdatedMixin, self).save_model(request, obj, form,
            change)


class PersonAdmin(CreatedUpdatedMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', ('short_name', 'long_name'),
            'suffix', 'image', 'date_of_birth', 'gender', 'biography', 'notes',
            'groups', 'tags']}),
        ('Publishing', {'fields': ['is_enabled', 'is_featured',
            ('created_at', 'created_by'), ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    list_display = ['__unicode__', email, phone, location, preview_image]
    list_filter = ['organisations', 'groups']
    readonly_fields = ['created_at', 'created_by',
        'updated_at', 'updated_by']
    inlines = [PersonOrganisationInline, ContactNicknameInline,
        ContactAddressInline, ContactEmailInline, ContactPhoneInline,
        ContactInstantMessengerHandleInline, ContactWebsiteInline]
    search_fields = ['short_name', 'long_name', 'nicknames__value',
        'emails__value', 'phones__value']

admin.site.register(Person, PersonAdmin)


class OrganisationAdmin(CreatedUpdatedMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'abn', 'image', 'biography',
            'notes', 'groups', 'tags']}),
        ('Publishing', {'fields': ['is_enabled', 'is_featured',
            ('created_at', 'created_by'), ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    list_display = ['name', email, phone, location, preview_image]
    list_filter = ['groups']
    readonly_fields = ['created_at', 'created_by',
        'updated_at', 'updated_by']
    inlines = [ContactNicknameInline, ContactAddressInline, ContactEmailInline,
        ContactPhoneInline, ContactInstantMessengerHandleInline,
        ContactWebsiteInline, OrganisationPersonInline]
    search_fields = ['name', 'abn', 'nicknames__value',
        'emails__value', 'phones__value']

admin.site.register(Organisation, OrganisationAdmin)


class ContactGroupAdmin(CreatedUpdatedMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'notes', 'tags']}),
        ('Publishing', {'fields': ['is_enabled', 'is_featured',
            ('created_at', 'created_by'), ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    list_display = ['name']
    readonly_fields = ['created_at', 'created_by',
        'updated_at', 'updated_by']
    search_fields = ['name']

admin.site.register(ContactGroup, ContactGroupAdmin)

