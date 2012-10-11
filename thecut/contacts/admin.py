# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.db import models
from django.forms import TextInput
from thecut.contacts.models import (ContactAddress, ContactGroup, ContactEmail,
    ContactInstantMessengerHandle, ContactNickname, ContactPhone, Organisation,
    Person, PersonOrganisation, ContactWebsite)


def email(obj):
    email = obj.get_email()
    return email and '<a href="mailto:%(email)s" ' \
        'title="%(title)s">%(email)s</a>' %(
        {'email': email, 'title': email.name}) or ''
email.allow_tags = True


def location(obj):
    address = obj.get_address()
    city = address and address.city or ''
    country = address and address.country or ''
    
    if city and country:
        return '%s, %s' %(city, country)
    else:
        return city or country or ''


def phone(obj):
    phone = obj.get_phone()
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


class NicknameInline(admin.TabularInline):
    extra = 0
    model = ContactNickname


class AddressInline(admin.StackedInline):
    extra = 0
    #fieldsets = [(None, {'fields': ['name', ('street', 'city'),
    #    ('state', 'postcode'), 'country']})]
    #formfield_overrides = {models.TextField: {'widget': TextInput(
    #    attrs={'class': 'vTextField'})}}
    model = ContactAddress


class EmailInline(admin.TabularInline):
    extra = 0
    model = ContactEmail
    verbose_name_plural = 'Email address'
    verbose_name_plural = 'Email addresses'


class InstantMessengerHandleInline(admin.TabularInline):
    extra = 0
    model = ContactInstantMessengerHandle
    verbose_name_plural = 'Instant messaging'


class PhoneInline(admin.TabularInline):
    extra = 0
    model = ContactPhone
    verbose_name = 'Phone number'
    verbose_name_plural = 'Phone numbers'


class WebsiteInline(admin.TabularInline):
    extra = 0
    model = ContactWebsite


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
        (None, {'fields': ['title', ('first_name', 'last_name'),
            'suffix', 'image', 'date_of_birth', 'biography', 'notes',
            'groups', 'tags']}),
        ('Publishing', {'fields': ['is_enabled', 'is_featured',
            ('created_at', 'created_by'), ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    list_display = ['__unicode__', email, phone, location, preview_image]
    list_filter = ['organisations', 'groups']
    readonly_fields = ['created_at', 'created_by',
        'updated_at', 'updated_by']
    inlines = [PersonOrganisationInline, NicknameInline, AddressInline,
        EmailInline, PhoneInline, InstantMessengerHandleInline,
        WebsiteInline]
    search_fields = ['first_name', 'last_name', 'nicknames__value',
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
    inlines = [NicknameInline, AddressInline, EmailInline, PhoneInline,
        InstantMessengerHandleInline, WebsiteInline,
        OrganisationPersonInline]
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

