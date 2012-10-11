# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from django_countries import CountryField
from model_utils.managers import PassThroughManager
from tagging.fields import TagField
from thecut.contacts import receivers, settings
from thecut.contacts.querysets import (AbstractContactGroupQuerySet,
    AbstractContactQuerySet, ContactAddressQuerySet, ContactEmailQuerySet)
import re


class AbstractAddress(models.Model):
    name = models.CharField(max_length=50, blank=True)
    street = models.TextField(blank=True)
    city = models.CharField(max_length=50, db_index=True, blank=True)
    state = models.CharField(max_length=50, db_index=True, blank=True)
    postcode = models.CharField(max_length=30, db_index=True, blank=True)
    country = CountryField(default=settings.DEFAULT_COUNTRY, db_index=True,
        blank=True)
    
    class Meta(object):
        abstract = True
    
    def __unicode__(self):
        return self.address
    
    @property
    def address(self):
        return ' '.join([self.street, self.city,
            self.state, self.postcode, unicode(self.country.name)])


class Address(AbstractAddress):
    pass


class AbstractEmail(models.Model):
    name = models.CharField(max_length=50, blank=True)
    value = models.EmailField('Email', max_length=75, db_index=True,
        blank=True)
    
    class Meta(object):
        abstract = True
    
    def __unicode__(self):
        return self.value
    
    def clean_fields(self, *args, **kwargs):
        super(AbstractEmail, self).clean_fields(*args, **kwargs)
        if not 'value' in kwargs.get('exclude', []):
            self.value = self.value.lower()


class Email(AbstractEmail):
    pass


class AbstractInstantMessengerHandle(models.Model):
    name = models.CharField(max_length=50, blank=True)
    value = models.CharField('ID', max_length=75, db_index=True, blank=True)
    type = models.CharField(max_length=50, db_index=True,
        choices=settings.INSTANT_MESSENGER_CHOICES, blank=True)
    
    class Meta(object):
        abstract = True
    
    def __unicode__(self):
        return self.value


class InstantMessengerHandle(AbstractInstantMessengerHandle):
    contact = models.ForeignKey('contacts.Contact',
        related_name='instant_messenger_handles')


class AbstractNickname(models.Model):
    value = models.CharField('Name', max_length=75, db_index=True, blank=True)
    
    class Meta(object):
        abstract = True
    
    def __unicode__(self):
        return self.value


class Nickname(AbstractNickname):
    contact = models.ForeignKey('contacts.Contact', related_name='nicknames')


class AbstractPhone(models.Model):
    name = models.CharField(max_length=50, blank=True)
    value = models.CharField('Number', max_length=75, db_index=True,
        blank=True)
    type = models.CharField(max_length=50, db_index=True,
        choices=settings.PHONE_TYPE_CHOICES, blank=True)
    
    class Meta(object):
        abstract = True
    
    def __unicode__(self):
        return self.value
    
    def clean_fields(self, *args, **kwargs):
        super(AbstractPhone, self).clean_fields(*args, **kwargs)
        if not 'value' in kwargs.get('exclude', []):
            self.value = re.sub('[^\d\+]+', '', self.value)


class Phone(AbstractPhone):
    contact = models.ForeignKey('contacts.Contact', related_name='phones')


class AbstractWebsite(models.Model):
    name = models.CharField(max_length=50, blank=True)
    value = models.URLField('URL', max_length=255, db_index=True, blank=True)
    
    class Meta(object):
        abstract = True
    
    def __unicode__(self):
        return self.value
    
    def clean_fields(self, *args, **kwargs):
        super(AbstractWebsite, self).clean_fields(*args, **kwargs)
        if not 'value' in kwargs.get('exclude', []):
            self.value = self.value.lower()


class Website(AbstractWebsite):
    contact = models.ForeignKey('contacts.Contact', related_name='websites')


class AbstractContactGroup(models.Model):
    
    name = models.CharField(max_length=150, db_index=True, blank=True)
    notes = models.TextField(blank=True)
    tags = TagField(blank=True, help_text='Separate tags with spaces, put ' \
        'quotes around multiple-word tags.')
    is_enabled = models.BooleanField('enabled', default=True)
    is_featured = models.BooleanField('featured', default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('auth.User', editable=False,
        related_name='+')
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey('auth.User', editable=False,
        related_name='+')
    objects = PassThroughManager().for_queryset_class(
        AbstractContactGroupQuerySet)()
    
    class Meta(object):
        abstract = True
        get_latest_by = 'created_at'
        ordering = ['name', '-created_at']
    
    def __unicode__(self):
        return self.name
    
    def is_active(self):
        return self in self.__class__.objects.active().filter(pk=self.pk)


class ContactGroup(AbstractContactGroup):
    
    class Meta(AbstractContactGroup.Meta):
        pass


class AbstractContact(models.Model):
    
    image = models.FileField(upload_to='uploads/contacts/images/%Y/%m/%d',
        blank=True, null=True)
    biography = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    tags = TagField(blank=True, help_text='Separate tags with spaces, put ' \
        'quotes around multiple-word tags.')
    is_enabled = models.BooleanField('enabled', default=True)
    is_featured = models.BooleanField('featured', default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('auth.User', editable=False,
        related_name='+')
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey('auth.User', editable=False,
        related_name='+')
    objects = PassThroughManager().for_queryset_class(AbstractContactQuerySet)()
    
    class Meta(object):
        abstract = True
        get_latest_by = 'created_at'
        ordering = ['-created_at']
    
    def is_active(self):
        return self in self.__class__.objects.active().filter(pk=self.pk)
    
    def _get_first_m2m_item(self, m2m_field):
        queryset = m2m_field.all()
        try:
            item = queryset[0]
        except IndexError:
            item = None
        return item
    
    def get_address(self):
        return self._get_first_m2m_item(self.addresses)
    
    def get_email(self):
        return self._get_first_m2m_item(self.emails)
    
    def get_nickname(self):
        return self._get_first_m2m_item(self.nicknames)
    
    def get_phone(self):
        return self._get_first_m2m_item(self.phones)
    
    def get_website(self):
        return self._get_first_m2m_item(self.websites)


class Contact(AbstractContact):
    
    groups = models.ManyToManyField('contacts.ContactGroup',
        related_name='contacts', blank=True, null=True)
    
    class Meta(AbstractContact.Meta):
        pass


class ContactAddress(models.Model):
    
    contact = models.ForeignKey('contacts.Contact', related_name='addresses')
    address = models.ForeignKey('contacts.Address', related_name='contacts')
    order = models.PositiveIntegerField(default=0)
    objects = PassThroughManager().for_queryset_class(ContactAddressQuerySet)()
    
    class Meta(object):
        ordering = ['order']
        unique_together = ['contact', 'address']
    
    def __unicode__(self):
        return unicode(self.address)

models.signals.pre_save.connect(receivers.set_order, sender=ContactAddress)


class ContactEmail(models.Model):
    
    contact = models.ForeignKey('contacts.Contact', related_name='emails')
    email = models.ForeignKey('contacts.Email', related_name='contacts')
    order = models.PositiveIntegerField(default=0)
    objects = PassThroughManager().for_queryset_class(ContactEmailQuerySet)()
    
    class Meta(object):
        ordering = ['order']
        unique_together = ['contact', 'email']
    
    def __unicode__(self):
        return unicode(self.email)

models.signals.pre_save.connect(receivers.set_order, sender=ContactEmail)



class PersonOrganisation(models.Model):
    person = models.ForeignKey('contacts.Person', related_name='occupations')
    organisation = models.ForeignKey('contacts.Organisation',
        related_name='positions')
    title = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    
    class Meta:
        verbose_name = 'employment'
        verbose_name_plural = 'employment'
    
    def __unicode__(self):
        organisation = unicode(self.organisation)
        person = unicode(self.person)
        title = self.title
        if organisation and person and title:
            return '%s: %s (%s)' %(organisation, person, title)
        elif organisation and person:
            return '%s: %s' %(organisation, person)
        else:
            return organisation or person


class AbstractPerson(Contact):
    title = models.CharField(max_length=15, blank=True)
    first_name = models.CharField(max_length=75, db_index=True, blank=True)
    last_name = models.CharField(max_length=75, db_index=True, blank=True)
    suffix = models.CharField(max_length=250, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    
    class Meta(Contact.Meta):
        abstract = True
        ordering = ['last_name', 'first_name']
    
    def __unicode__(self):
        return self.name or 'Unnamed'
    
    @property
    def name(self):
        if self.first_name and self.last_name:
            return ' '.join([self.first_name, self.last_name])
        else:
            return self.first_name or self.last_name or None


class Person(AbstractPerson):
    user = models.OneToOneField('auth.User', related_name='contact',
        blank=True, null=True)
    organisations = models.ManyToManyField('contacts.Organisation',
        related_name='people', through='contacts.PersonOrganisation',
        blank=True, null=True)
    
    class Meta(AbstractPerson.Meta):
        verbose_name_plural = 'people'


class AbstractOrganisation(Contact):
    name = models.CharField(max_length=150, db_index=True, blank=True)
    abn = models.CharField('ABN', max_length=11, db_index=True, blank=True)
    
    class Meta(Contact.Meta):
        abstract = True
        ordering = ['name']
    
    def __unicode__(self):
        return self.name


class Organisation(AbstractOrganisation):
    
    class Meta(AbstractOrganisation.Meta):
        pass

