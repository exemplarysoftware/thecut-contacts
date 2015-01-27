# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django_countries import CountryField
from model_utils.managers import PassThroughManager
from taggit.managers import TaggableManager
from thecut.authorship.models import Authorship
from thecut.contacts import choices, receivers, settings
from thecut.contacts.querysets import ActiveFeaturedQuerySet, QuerySet
import re
import warnings


@python_2_unicode_compatible
class AbstractAddress(models.Model):

    name = models.CharField(max_length=250, blank=True)

    street = models.TextField(blank=True)

    city = models.CharField(max_length=250, db_index=True, blank=True)

    state = models.CharField(max_length=250, db_index=True, blank=True)

    postcode = models.CharField(max_length=50, db_index=True, blank=True)

    country = CountryField(default=settings.DEFAULT_COUNTRY, db_index=True,
                           blank=True)

    objects = PassThroughManager().for_queryset_class(QuerySet)()

    class Meta(object):
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.address

    @property
    def address(self):
        items = [self.street, self.city, self.state, self.postcode,
                 '{0}'.format(self.country.name)]
        return ' '.join(filter(bool, items))


class Address(AbstractAddress):

    class Meta(AbstractAddress.Meta):
        ordering = ['contact_addresses__order']


@python_2_unicode_compatible
class AbstractEmail(models.Model):

    name = models.CharField(max_length=250, blank=True)

    value = models.EmailField('Email', max_length=254, db_index=True,
                              blank=True)

    objects = PassThroughManager().for_queryset_class(QuerySet)()

    class Meta(object):
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.value

    def clean_fields(self, *args, **kwargs):
        super(AbstractEmail, self).clean_fields(*args, **kwargs)
        if 'value' not in kwargs.get('exclude', []):
            self.value = self.value.lower()


class Email(AbstractEmail):

    class Meta(AbstractEmail.Meta):
        ordering = ['contact_emails__order']


@python_2_unicode_compatible
class AbstractInstantMessengerHandle(models.Model):

    name = models.CharField(max_length=250, blank=True)

    value = models.CharField('ID', max_length=254, db_index=True, blank=True)

    type = models.CharField(max_length=50, db_index=True,
                            choices=choices.INSTANT_MESSENGER_TYPES,
                            blank=True)

    objects = PassThroughManager().for_queryset_class(QuerySet)()

    class Meta(object):
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.value


class InstantMessengerHandle(AbstractInstantMessengerHandle):

    class Meta(AbstractInstantMessengerHandle.Meta):
        ordering = ['contact_instant_messenger_handles__order']


@python_2_unicode_compatible
class AbstractNickname(models.Model):

    value = models.CharField('Name', max_length=250, db_index=True, blank=True)

    objects = PassThroughManager().for_queryset_class(QuerySet)()

    class Meta(object):
        abstract = True
        ordering = ['value']

    def __str__(self):
        return self.value


class Nickname(AbstractNickname):

    class Meta(AbstractNickname.Meta):
        ordering = ['contact_nicknames__order']


@python_2_unicode_compatible
class AbstractPhone(models.Model):

    name = models.CharField(max_length=250, blank=True)

    value = models.CharField('Number', max_length=250, db_index=True,
                             blank=True)

    type = models.CharField(max_length=50, db_index=True,
                            choices=choices.PHONE_TYPES, blank=True)

    objects = PassThroughManager().for_queryset_class(QuerySet)()

    class Meta(object):
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.value

    def clean_fields(self, *args, **kwargs):
        super(AbstractPhone, self).clean_fields(*args, **kwargs)
        if 'value' not in kwargs.get('exclude', []):
            self.value = re.sub('[^\d\+]+', '', self.value)


class Phone(AbstractPhone):

    class Meta(AbstractPhone.Meta):
        ordering = ['contact_phones__order']


@python_2_unicode_compatible
class AbstractWebsite(models.Model):

    name = models.CharField(max_length=250, blank=True)

    value = models.URLField('URL', max_length=255, db_index=True, blank=True)

    objects = PassThroughManager().for_queryset_class(QuerySet)()

    class Meta(object):
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.value

    def clean_fields(self, *args, **kwargs):
        super(AbstractWebsite, self).clean_fields(*args, **kwargs)
        if 'value' not in kwargs.get('exclude', []):
            self.value = self.value.lower()


class Website(AbstractWebsite):

    class Meta(AbstractWebsite.Meta):
        ordering = ['contact_websites__order']


@python_2_unicode_compatible
class AbstractContactGroup(Authorship):

    name = models.CharField(max_length=250, db_index=True, blank=True)

    notes = models.TextField(blank=True)

    tags = TaggableManager(blank=True, related_name='+contactgroups')

    is_enabled = models.BooleanField('enabled', default=True)

    is_featured = models.BooleanField('featured', default=False)

    objects = PassThroughManager().for_queryset_class(ActiveFeaturedQuerySet)()

    class Meta(Authorship.Meta):
        abstract = True
        get_latest_by = 'created_at'
        ordering = ('name', '-created_at')

    def __str__(self):
        return self.name

    def is_active(self):
        return self in self.__class__.objects.active().filter(pk=self.pk)


class ContactGroup(AbstractContactGroup):

    class Meta(AbstractContactGroup.Meta):
        pass


class AbstractContact(Authorship):

    image = models.FileField(upload_to='uploads/contacts/images/%Y/%m/%d',
                             blank=True, null=True)

    biography = models.TextField(blank=True)

    notes = models.TextField(blank=True)

    tags = TaggableManager(blank=True, related_name='+contacts')

    is_enabled = models.BooleanField('enabled', default=True)

    is_featured = models.BooleanField('featured', default=False)

    objects = PassThroughManager().for_queryset_class(ActiveFeaturedQuerySet)()

    class Meta(Authorship.Meta):
        abstract = True
        get_latest_by = 'created_at'
        ordering = ('-created_at',)

    def is_active(self):
        return self.__class__.objects.active().filter(pk=self.pk).exists()

models.signals.pre_save.connect(receivers.check_and_delete_image)
models.signals.pre_delete.connect(receivers.delete_image)


class Contact(AbstractContact):

    groups = models.ManyToManyField('contacts.ContactGroup',
                                    related_name='contacts', blank=True,
                                    null=True)

    addresses = models.ManyToManyField('contacts.Address', related_name='+',
                                       through='contacts.ContactAddress',
                                       blank=True, null=True)

    emails = models.ManyToManyField('contacts.Email', related_name='+',
                                    through='contacts.ContactEmail',
                                    blank=True, null=True)

    instant_messenger_handles = models.ManyToManyField(
        'contacts.InstantMessengerHandle', related_name='+',
        through='contacts.ContactInstantMessengerHandle', blank=True,
        null=True)

    nicknames = models.ManyToManyField('contacts.Nickname', related_name='+',
                                       through='contacts.ContactNickname',
                                       blank=True, null=True)

    phones = models.ManyToManyField('contacts.Phone', related_name='+',
                                    through='contacts.ContactPhone',
                                    blank=True, null=True)

    websites = models.ManyToManyField('contacts.Website', related_name='+',
                                      through='contacts.ContactWebsite',
                                      blank=True, null=True)

    class Meta(AbstractContact.Meta):
        pass

    def get_address(self):
        """Deprecated - instead use 'addresses.get_first()'."""
        warnings.warn('\'get_address\' method is deprecated - use '
                      '\'addresses.get_first()\' method.', DeprecationWarning,
                      stacklevel=2)
        return self.addresses.get_first()

    def get_email(self):
        """Deprecated - instead use 'emails.get_first()'."""
        warnings.warn('\'get_email\' method is deprecated - use '
                      '\'emails.get_first()\' method.', DeprecationWarning,
                      stacklevel=2)
        return self.emails.get_first()

    def get_nickname(self):
        """Deprecated - instead use 'nicknames.get_first()'."""
        warnings.warn('\'get_nickname\' method is deprecated - use '
                      '\'nicknames.get_first()\' method.', DeprecationWarning,
                      stacklevel=2)
        return self.nicknames.get_first()

    def get_phone(self):
        """Deprecated - instead use 'phones.get_first()'."""
        warnings.warn('\'get_phone\' method is deprecated - use '
                      '\'phones.get_first()\' method.', DeprecationWarning,
                      stacklevel=2)
        return self.phones.get_first()

    def get_website(self):
        """Deprecated - instead use 'websites.get_first()'."""
        warnings.warn('\'get_website\' method is deprecated - use '
                      '\'websites.get_first()\' method.', DeprecationWarning,
                      stacklevel=2)
        return self.websites.get_first()


@python_2_unicode_compatible
class ContactAddress(models.Model):

    contact = models.ForeignKey('contacts.Contact', related_name='+')

    address = models.ForeignKey('contacts.Address',
                                related_name='contact_addresses')

    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ('order',)
        unique_together = ('contact', 'address')

    def __str__(self):
        return '{0}'.format(self.address)

models.signals.pre_save.connect(receivers.set_order, sender=ContactAddress)
models.signals.post_delete.connect(receivers.delete_related_address,
                                   sender=ContactAddress)


@python_2_unicode_compatible
class ContactEmail(models.Model):

    contact = models.ForeignKey('contacts.Contact', related_name='+')

    email = models.ForeignKey('contacts.Email', related_name='contact_emails')

    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ('order',)
        unique_together = ('contact', 'email')

    def __str__(self):
        return '{0}'.format(self.email)

models.signals.pre_save.connect(receivers.set_order, sender=ContactEmail)
models.signals.post_delete.connect(receivers.delete_related_email,
                                   sender=ContactEmail)


@python_2_unicode_compatible
class ContactInstantMessengerHandle(models.Model):

    contact = models.ForeignKey('contacts.Contact', related_name='+')

    instant_messenger_handle = models.ForeignKey(
        'contacts.InstantMessengerHandle',
        related_name='contact_instant_messenger_handles')

    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ('order',)
        unique_together = ('contact', 'instant_messenger_handle')

    def __str__(self):
        return '{0}'.format(self.instant_messenger_handle)

models.signals.pre_save.connect(receivers.set_order,
                                sender=ContactInstantMessengerHandle)
models.signals.post_delete.connect(
    receivers.delete_related_instant_messenger_handle,
    sender=ContactInstantMessengerHandle)


@python_2_unicode_compatible
class ContactNickname(models.Model):

    contact = models.ForeignKey('contacts.Contact', related_name='+')

    nickname = models.ForeignKey('contacts.Nickname',
                                 related_name='contact_nicknames')

    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ('order',)
        unique_together = ('contact', 'nickname')

    def __str__(self):
        return '{0}'.format(self.nickname)

models.signals.pre_save.connect(receivers.set_order, sender=ContactNickname)
models.signals.post_delete.connect(receivers.delete_related_nickname,
                                   sender=ContactNickname)


@python_2_unicode_compatible
class ContactPhone(models.Model):

    contact = models.ForeignKey('contacts.Contact', related_name='+')

    phone = models.ForeignKey('contacts.Phone', related_name='contact_phones')

    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ('order',)
        unique_together = ('contact', 'phone')

    def __str__(self):
        return '{0}'.format(self.phone)

models.signals.pre_save.connect(receivers.set_order, sender=ContactPhone)
models.signals.post_delete.connect(receivers.delete_related_phone,
                                   sender=ContactPhone)


@python_2_unicode_compatible
class ContactWebsite(models.Model):

    contact = models.ForeignKey('contacts.Contact', related_name='+')

    website = models.ForeignKey('contacts.Website',
                                related_name='contact_websites')

    order = models.PositiveIntegerField(default=0)

    class Meta(object):
        ordering = ('order',)
        unique_together = ('contact', 'website')

    def __str__(self):
        return '{0}'.format(self.website)

models.signals.pre_save.connect(receivers.set_order, sender=ContactWebsite)
models.signals.post_delete.connect(receivers.delete_related_website,
                                   sender=ContactWebsite)


@python_2_unicode_compatible
class PersonOrganisation(models.Model):

    person = models.ForeignKey('contacts.Person', related_name='occupations')

    organisation = models.ForeignKey('contacts.Organisation',
                                     related_name='positions')

    title = models.CharField(max_length=250, blank=True)

    department = models.CharField(max_length=250, blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'employment'
        verbose_name_plural = 'employment'

    def __str__(self):
        if self.organisation and self.person and self.title:
            return '{0}: {1} ({2})'.format(self.organisation, self.person,
                                           self.title)
        elif self.organisation and self.person:
            return '{0}: {1}'.format(self.organisation, self.person)
        else:
            return self.organisation or self.person

models.signals.pre_save.connect(receivers.set_personorganisation_order,
                                sender=PersonOrganisation)


@python_2_unicode_compatible
class AbstractPerson(Contact):

    title = models.CharField(max_length=250, blank=True)

    short_name = models.CharField(max_length=250, db_index=True, blank=True)

    long_name = models.CharField(max_length=250, db_index=True, blank=True)

    suffix = models.CharField(max_length=250, blank=True)

    date_of_birth = models.DateField(blank=True, null=True)

    gender = models.CharField(max_length=1, blank=True, default='',
                              choices=choices.GENDERS)

    class Meta(Contact.Meta):
        abstract = True
        ordering = ('long_name',)

    def __str__(self):
        return self.name or 'Unnamed'

    @property
    def name(self):
        return self.long_name or self.short_name or None


class Person(AbstractPerson):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True,
                                null=True, related_name='contact')

    organisations = models.ManyToManyField(
        'contacts.Organisation', related_name='people',
        through='contacts.PersonOrganisation', blank=True, null=True)

    class Meta(AbstractPerson.Meta):
        verbose_name_plural = 'people'


@python_2_unicode_compatible
class AbstractOrganisation(Contact):

    name = models.CharField(max_length=250, db_index=True, blank=True)

    abn = models.CharField('ABN', max_length=11, db_index=True, blank=True)

    class Meta(Contact.Meta):
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return self.name


class Organisation(AbstractOrganisation):

    class Meta(AbstractOrganisation.Meta):
        pass
