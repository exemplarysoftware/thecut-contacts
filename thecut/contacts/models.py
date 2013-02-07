# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from django_countries import CountryField
from model_utils.managers import PassThroughManager
from tagging.fields import TagField
from thecut.contacts import choices, receivers, settings
from thecut.contacts.querysets import ActiveFeaturedQuerySet, QuerySet
import re
import warnings


class AbstractAddress(models.Model):

    name = models.CharField(max_length=50, blank=True)
    street = models.TextField(blank=True)
    city = models.CharField(max_length=50, db_index=True, blank=True)
    state = models.CharField(max_length=50, db_index=True, blank=True)
    postcode = models.CharField(max_length=30, db_index=True, blank=True)
    country = CountryField(default=settings.DEFAULT_COUNTRY, db_index=True,
        blank=True)
    objects = PassThroughManager().for_queryset_class(QuerySet)()

    class Meta(object):
        abstract = True
        ordering = ['contact_addresses__order']

    def __unicode__(self):
        return self.address

    @property
    def address(self):
        items = [self.street, self.city, self.state, self.postcode,
            unicode(self.country.name)]
        return ' '.join(filter(bool, items))


class Address(AbstractAddress):

    pass


class AbstractEmail(models.Model):

    name = models.CharField(max_length=50, blank=True)
    value = models.EmailField('Email', max_length=75, db_index=True,
        blank=True)
    objects = PassThroughManager().for_queryset_class(QuerySet)()

    class Meta(object):
        abstract = True
        ordering = ['contact_emails__order']

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
        choices=choices.INSTANT_MESSENGER_TYPES, blank=True)
    objects = PassThroughManager().for_queryset_class(QuerySet)()

    class Meta(object):
        abstract = True
        ordering = ['contact_instant_messenger_handles__order']

    def __unicode__(self):
        return self.value


class InstantMessengerHandle(AbstractInstantMessengerHandle):

    pass


class AbstractNickname(models.Model):

    value = models.CharField('Name', max_length=75, db_index=True, blank=True)
    objects = PassThroughManager().for_queryset_class(QuerySet)()

    class Meta(object):
        abstract = True
        ordering = ['contact_nicknames__order']

    def __unicode__(self):
        return self.value


class Nickname(AbstractNickname):

    pass


class AbstractPhone(models.Model):

    name = models.CharField(max_length=50, blank=True)
    value = models.CharField('Number', max_length=75, db_index=True,
        blank=True)
    type = models.CharField(max_length=50, db_index=True,
        choices=choices.PHONE_TYPES, blank=True)
    objects = PassThroughManager().for_queryset_class(QuerySet)()

    class Meta(object):
        abstract = True
        ordering = ['contact_phones__order']

    def __unicode__(self):
        return self.value

    def clean_fields(self, *args, **kwargs):
        super(AbstractPhone, self).clean_fields(*args, **kwargs)
        if not 'value' in kwargs.get('exclude', []):
            self.value = re.sub('[^\d\+]+', '', self.value)


class Phone(AbstractPhone):

    pass


class AbstractWebsite(models.Model):

    name = models.CharField(max_length=50, blank=True)
    value = models.URLField('URL', max_length=255, db_index=True, blank=True)
    objects = PassThroughManager().for_queryset_class(QuerySet)()

    class Meta(object):
        abstract = True
        ordering = ['contact_websites__order']

    def __unicode__(self):
        return self.value

    def clean_fields(self, *args, **kwargs):
        super(AbstractWebsite, self).clean_fields(*args, **kwargs)
        if not 'value' in kwargs.get('exclude', []):
            self.value = self.value.lower()


class Website(AbstractWebsite):

    pass


class AbstractContactGroup(models.Model):

    name = models.CharField(max_length=150, db_index=True, blank=True)
    notes = models.TextField(blank=True)
    tags = TagField(blank=True, help_text='Separate tags with spaces, put ' \
        'quotes around multiple-word tags.')
    is_enabled = models.BooleanField('enabled', default=True)
    is_featured = models.BooleanField('featured', default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False,
        related_name='+')
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False,
        related_name='+')
    objects = PassThroughManager().for_queryset_class(ActiveFeaturedQuerySet)()

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
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False,
        related_name='+')
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False,
        related_name='+')
    objects = PassThroughManager().for_queryset_class(ActiveFeaturedQuerySet)()

    class Meta(object):
        abstract = True
        get_latest_by = 'created_at'
        ordering = ['-created_at']

    def is_active(self):
        return self.__class__.objects.active().filter(pk=self.pk).exists()

models.signals.pre_save.connect(receivers.check_and_delete_image)
models.signals.pre_delete.connect(receivers.delete_image)


class Contact(AbstractContact):

    groups = models.ManyToManyField('contacts.ContactGroup',
        related_name='contacts', blank=True, null=True)
    addresses = models.ManyToManyField('contacts.Address', related_name='+',
        through='contacts.ContactAddress', blank=True, null=True)
    emails = models.ManyToManyField('contacts.Email', related_name='+',
        through='contacts.ContactEmail', blank=True, null=True)
    instant_messenger_handles = models.ManyToManyField(
        'contacts.InstantMessengerHandle', related_name='+',
        through='contacts.ContactInstantMessengerHandle', blank=True, null=True)
    nicknames = models.ManyToManyField('contacts.Nickname', related_name='+',
        through='contacts.ContactNickname', blank=True, null=True)
    phones = models.ManyToManyField('contacts.Phone', related_name='+',
        through='contacts.ContactPhone', blank=True, null=True)
    websites = models.ManyToManyField('contacts.Website', related_name='+',
        through='contacts.ContactWebsite', blank=True, null=True)

    class Meta(AbstractContact.Meta):
        pass

    def get_address(self):
        """Deprecated - instead use 'addresses.get_first()'."""
        warnings.warn('\'get_address\' method is deprecated - use ' \
            '\'addresses.get_first()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.addresses.get_first()

    def get_email(self):
        """Deprecated - instead use 'emails.get_first()'."""
        warnings.warn('\'get_email\' method is deprecated - use ' \
            '\'emails.get_first()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.emails.get_first()

    def get_nickname(self):
        """Deprecated - instead use 'nicknames.get_first()'."""
        warnings.warn('\'get_nickname\' method is deprecated - use ' \
            '\'nicknames.get_first()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.nicknames.get_first()

    def get_phone(self):
        """Deprecated - instead use 'phones.get_first()'."""
        warnings.warn('\'get_phone\' method is deprecated - use ' \
            '\'phones.get_first()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.phones.get_first()

    def get_website(self):
        """Deprecated - instead use 'websites.get_first()'."""
        warnings.warn('\'get_website\' method is deprecated - use ' \
            '\'websites.get_first()\' method.', DeprecationWarning,
            stacklevel=2)
        return self.websites.get_first()


class ContactAddress(models.Model):

    contact = models.ForeignKey('contacts.Contact', related_name='+')
    address = models.ForeignKey('contacts.Address',
        related_name='contact_addresses')
    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ['order']
        unique_together = ['contact', 'address']

    def __unicode__(self):
        return unicode(self.address)

models.signals.pre_save.connect(receivers.set_order, sender=ContactAddress)
models.signals.post_delete.connect(receivers.delete_related_address,
    sender=ContactAddress)


class ContactEmail(models.Model):

    contact = models.ForeignKey('contacts.Contact', related_name='+')
    email = models.ForeignKey('contacts.Email', related_name='contact_emails')
    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ['order']
        unique_together = ['contact', 'email']

    def __unicode__(self):
        return unicode(self.email)

models.signals.pre_save.connect(receivers.set_order, sender=ContactEmail)
models.signals.post_delete.connect(receivers.delete_related_email,
    sender=ContactEmail)


class ContactInstantMessengerHandle(models.Model):

    contact = models.ForeignKey('contacts.Contact', related_name='+')
    instant_messenger_handle = models.ForeignKey(
        'contacts.InstantMessengerHandle',
        related_name='contact_instant_messenger_handles')
    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ['order']
        unique_together = ['contact', 'instant_messenger_handle']

    def __unicode__(self):
        return unicode(self.instant_messenger_handle)

models.signals.pre_save.connect(receivers.set_order,
    sender=ContactInstantMessengerHandle)
models.signals.post_delete.connect(
    receivers.delete_related_instant_messenger_handle,
    sender=ContactInstantMessengerHandle)


class ContactNickname(models.Model):

    contact = models.ForeignKey('contacts.Contact', related_name='+')
    nickname = models.ForeignKey('contacts.Nickname',
        related_name='contact_nicknames')
    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ['order']
        unique_together = ['contact', 'nickname']

    def __unicode__(self):
        return unicode(self.nickname)

models.signals.pre_save.connect(receivers.set_order, sender=ContactNickname)
models.signals.post_delete.connect(receivers.delete_related_nickname,
    sender=ContactNickname)


class ContactPhone(models.Model):

    contact = models.ForeignKey('contacts.Contact', related_name='+')
    phone = models.ForeignKey('contacts.Phone', related_name='contact_phones')
    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ['order']
        unique_together = ['contact', 'phone']

    def __unicode__(self):
        return unicode(self.phone)

models.signals.pre_save.connect(receivers.set_order, sender=ContactPhone)
models.signals.post_delete.connect(receivers.delete_related_phone,
    sender=ContactPhone)


class ContactWebsite(models.Model):

    contact = models.ForeignKey('contacts.Contact', related_name='+')
    website = models.ForeignKey('contacts.Website',
        related_name='contact_websites')
    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ['order']
        unique_together = ['contact', 'website']

    def __unicode__(self):
        return unicode(self.website)

models.signals.pre_save.connect(receivers.set_order, sender=ContactWebsite)
models.signals.post_delete.connect(receivers.delete_related_website,
    sender=ContactWebsite)


class PersonOrganisation(models.Model):

    person = models.ForeignKey('contacts.Person', related_name='occupations')
    organisation = models.ForeignKey('contacts.Organisation',
        related_name='positions')
    title = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

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

models.signals.pre_save.connect(receivers.set_personorganisation_order,
    sender=PersonOrganisation)


class AbstractPerson(Contact):

    title = models.CharField(max_length=15, blank=True)
    short_name = models.CharField(max_length=250, db_index=True, blank=True)
    long_name = models.CharField(max_length=250, db_index=True, blank=True)
    suffix = models.CharField(max_length=250, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, default='',
        choices=choices.GENDERS)

    class Meta(Contact.Meta):
        abstract = True
        ordering = ['long_name']

    def __unicode__(self):
        return self.name or 'Unnamed'

    @property
    def name(self):
        return self.long_name or self.short_name or None


class Person(AbstractPerson):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                blank=True, null=True, related_name='contact')
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
