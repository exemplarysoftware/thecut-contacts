# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from django_countries import countries
from thecut.contacts import choices, settings
from thecut.contacts.models import (
    Address, ContactAddress, Email, ContactEmail, InstantMessengerHandle,
    ContactInstantMessengerHandle, Nickname, ContactNickname, Phone,
    ContactPhone, Website, ContactWebsite)


class ContactRelatedInlineForm(forms.ModelForm):
    """Form which will also populate/save a related object."""

    _related_fields = []
    _related_name = None
    _related_class = None

    def __init__(self, *args, **kwargs):
        super(ContactRelatedInlineForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            related_instance = getattr(self.instance, self._related_name)
            related_data = forms.models.model_to_dict(
                related_instance, fields=self._related_fields)
            for key, value in related_data.items():
                self.fields[key].initial = value

    def save(self, *args, **kwargs):
        try:
            related_instance = getattr(self.instance, self._related_name)
        except self._related_class.DoesNotExist:
            related_instance = self._related_class()

        related_obj = forms.models.save_instance(self, related_instance,
                                                 fields=self._related_fields)
        setattr(self.instance, self._related_name, related_obj)

        return super(ContactRelatedInlineForm, self).save(*args, **kwargs)


class ContactAddressInlineForm(ContactRelatedInlineForm):

    name = forms.CharField(label='Name', max_length=50, required=False)

    street = forms.CharField(label='Street', required=False)

    city = forms.CharField(label='City', max_length=50, required=False)

    state = forms.CharField(label='State', max_length=50, required=False)

    postcode = forms.CharField(label='Postcode', max_length=30, required=False)

    country = forms.ChoiceField(label='Country', choices=countries,
                                initial=settings.DEFAULT_COUNTRY,
                                required=False)

    _related_fields = ('name', 'street', 'city', 'state', 'postcode',
                       'country')
    _related_name = 'address'
    _related_class = Address

    class Meta(object):
        exclude = ('address',)
        model = ContactAddress


class ContactEmailInlineForm(ContactRelatedInlineForm):

    name = forms.CharField(label='Name', max_length=50, required=False)

    value = forms.EmailField(label='Email', max_length=75)

    _related_fields = ('name', 'value')
    _related_name = 'email'
    _related_class = Email

    class Meta(object):
        exclude = ('email',)
        model = ContactEmail


class ContactInstantMessengerHandleInlineForm(ContactRelatedInlineForm):

    name = forms.CharField(label='Name', max_length=50, required=False)

    value = forms.CharField(label='ID', max_length=75)

    type = forms.ChoiceField(
        label='Type', choices=[('', '')]+choices.INSTANT_MESSENGER_TYPES,
        required=False)

    _related_fields = ('name', 'value', 'type')
    _related_name = 'instant_messenger_handle'
    _related_class = InstantMessengerHandle

    class Meta(object):
        exclude = ('instant_messenger_handle',)
        model = ContactInstantMessengerHandle


class ContactNicknameInlineForm(ContactRelatedInlineForm):

    value = forms.CharField(label='Name', max_length=75)

    _related_fields = ('value',)
    _related_name = 'nickname'
    _related_class = Nickname

    class Meta(object):
        exclude = ('nickname',)
        model = ContactNickname


class ContactPhoneInlineForm(ContactRelatedInlineForm):

    name = forms.CharField(label='Name', max_length=50, required=False)

    value = forms.CharField(label='Number', max_length=75)

    type = forms.ChoiceField(label='Type',
                             choices=[('', '')]+choices.PHONE_TYPES,
                             required=False)

    _related_fields = ('name', 'value', 'type')
    _related_name = 'phone'
    _related_class = Phone

    class Meta(object):
        exclude = ('phone',)
        model = ContactPhone


class ContactWebsiteInlineForm(ContactRelatedInlineForm):

    name = forms.CharField(label='Name', max_length=50, required=False)

    value = forms.URLField(label='URL', max_length=255)

    _related_fields = ('name', 'value')
    _related_name = 'website'
    _related_class = Website

    class Meta(object):
        exclude = ('website',)
        model = ContactWebsite
