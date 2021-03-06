# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import forms
from .models import (ContactAddress, ContactGroup, ContactEmail,
                     ContactInstantMessengerHandle, ContactNickname,
                     ContactPhone, Organisation, Person, PersonOrganisation,
                     ContactWebsite)
from django.contrib import admin
from django.utils.html import format_html
from thecut.authorship.admin import AuthorshipMixin


def email(obj):
    email = obj.emails.first()
    if email:
        return format_html(
            '<a href="mailto:{email}" title="{name}">{email}</a>',
            email=email, name=email.name)
    else:
        return ''


def location(obj):
    address = obj.addresses.first()
    if address:
        country = '{}'.format(address.country)
        return ', '.join(filter(bool, [address.city, country]))
    else:
        return ''


def phone(obj):
    phone = obj.phones.first()
    if phone:
        return '{}'.format(phone)
    else:
        return ''


def preview_image(obj):
    html = ''
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
                html = format_html('<img src="{}" alt="{}" />', thumb.url, obj)
    return html
preview_image.short_description = 'Image'


class ContactAddressInline(admin.StackedInline):

    extra = 0

    fieldsets = [
        (None, {'fields': ['name', ('street', 'city'),
                           ('state', 'postcode'), 'country']}),
    ]

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

    fields = ['organisation', 'title', 'department']

    model = PersonOrganisation

    verbose_name = 'Organisation'

    verbose_name_plural = 'Organisations'


class OrganisationPersonInline(admin.TabularInline):

    extra = 0

    fields = ['person', 'title', 'department']

    model = PersonOrganisation

    verbose_name = 'Person'

    verbose_name_plural = 'People'


class PersonAdmin(AuthorshipMixin, admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['title', ('short_name', 'long_name'), 'suffix',
                           'image', 'date_of_birth', 'gender', 'biography',
                           'notes', 'groups', 'tags']}),
        ('Publishing', {'fields': ['is_enabled', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')],
                        'classes': ['collapse']}),
    ]

    list_display = ['name', email, phone, location, preview_image]

    list_filter = ['organisations', 'groups']

    readonly_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

    inlines = [PersonOrganisationInline, ContactNicknameInline,
               ContactAddressInline, ContactEmailInline, ContactPhoneInline,
               ContactInstantMessengerHandleInline, ContactWebsiteInline]

    search_fields = ['short_name', 'long_name', 'nicknames__value',
                     'emails__value', 'phones__value']

admin.site.register(Person, PersonAdmin)


class OrganisationAdmin(AuthorshipMixin, admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name', 'abn', 'image', 'biography', 'notes',
                           'groups', 'tags']}),
        ('Publishing', {'fields': ['is_enabled', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')],
                        'classes': ['collapse']}),
    ]

    list_display = ['name', email, phone, location, preview_image]

    list_filter = ['groups']

    readonly_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

    inlines = [ContactNicknameInline, ContactAddressInline, ContactEmailInline,
               ContactPhoneInline, ContactInstantMessengerHandleInline,
               ContactWebsiteInline, OrganisationPersonInline]

    search_fields = ['name', 'abn', 'nicknames__value', 'emails__value',
                     'phones__value']

admin.site.register(Organisation, OrganisationAdmin)


class ContactGroupAdmin(AuthorshipMixin, admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name', 'notes', 'tags']}),
        ('Publishing', {'fields': ['is_enabled', 'is_featured',
                                   ('created_at', 'created_by'),
                                   ('updated_at', 'updated_by')],
                        'classes': ['collapse']}),
    ]

    list_display = ['name']

    readonly_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

    search_fields = ['name']

admin.site.register(ContactGroup, ContactGroupAdmin)
