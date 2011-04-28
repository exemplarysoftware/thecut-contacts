from django.db import models
from django_countries import CountryField
from tagging.fields import TagField
from thecut.core.managers import QuerySetManager
from thecut.core.models import AbstractBaseResource
from thecut.contacts.settings import DEFAULT_COUNTRY, \
    INSTANT_MESSENGER_TYPES, PHONE_TYPES
import re


class Address(models.Model):
    contact = models.ForeignKey('contacts.Contact',
        related_name='addresses')
    name = models.CharField(max_length=50, blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, db_index=True,
        blank=True, null=True)
    state = models.CharField(max_length=50, db_index=True,
        blank=True, null=True)
    postcode = models.CharField(max_length=30, db_index=True,
        blank=True, null=True)
    country = CountryField(default=DEFAULT_COUNTRY, db_index=True, blank=True,
        null=True)
    
    def __unicode__(self):
        return self.address
    
    @property
    def address(self):
        return ' '.join([self.street, self.city,
            self.state, self.postcode, unicode(self.country.name)])


class Email(models.Model):
    contact = models.ForeignKey('contacts.Contact',
        related_name='emails')
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.EmailField('Email', max_length=75, db_index=True,
        blank=True, null=True)
    
    def __unicode__(self):
        return self.value
    
    def clean_fields(self, *args, **kwargs):
        super(Email, self).clean_fields(*args, **kwargs)
        if not 'value' in kwargs.get('exclude', []):
            self.value = self.value.lower()


class InstantMessengerHandle(models.Model):
    contact = models.ForeignKey('contacts.Contact',
        related_name='instant_messenger_handles')
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField('ID', max_length=75, db_index=True,
        blank=True, null=True)
    type = models.CharField(max_length=50, db_index=True,
        choices=INSTANT_MESSENGER_TYPES, blank=True, null=True)
    
    def __unicode__(self):
        return self.value


class Nickname(models.Model):
    contact = models.ForeignKey('contacts.Contact',
        related_name='nicknames')
    value = models.CharField('Name', max_length=75, db_index=True,
        blank=True, null=True)
    
    def __unicode__(self):
        return self.value


class Phone(models.Model):
    contact = models.ForeignKey('contacts.Contact',
        related_name='phones')
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField('Number / address', max_length=75, db_index=True,
        blank=True, null=True)
    type = models.CharField(max_length=50, db_index=True,
        choices=PHONE_TYPES, blank=True, null=True)
    
    def __unicode__(self):
        return self.value
    
    def clean_fields(self, *args, **kwargs):
        super(Phone, self).clean_fields(*args, **kwargs)
        if not 'value' in kwargs.get('exclude', []):
            self.value = re.sub('[^\d\+]+', '', self.value)


class Website(models.Model):
    contact = models.ForeignKey('contacts.Contact',
        related_name='websites')
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.URLField('URL', max_length=255, db_index=True,
        blank=True, null=True)
    
    def __unicode__(self):
        return self.value
    
    def clean_fields(self, *args, **kwargs):
        super(Website, self).clean_fields(*args, **kwargs)
        if not 'value' in kwargs.get('exclude', []):
            self.value = self.value.lower()


class ContactGroup(AbstractBaseResource):
    name = models.CharField(max_length=150, db_index=True,
        blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    tags = TagField(blank=True, null=True, help_text='Separate tags \
        with spaces, put quotes around multiple-word tags.')
    
    objects = QuerySetManager()
    
    class Meta(AbstractBaseResource.Meta):
        ordering = ['name']
    
    def __unicode__(self):
        return self.name


class Contact(AbstractBaseResource):
    groups = models.ManyToManyField('contacts.ContactGroup',
        related_name='contacts', blank=True, null=True)
    image = models.FileField(
        upload_to='uploads/contacts/images/%Y/%m/%d',
        blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    tags = TagField(blank=True, null=True, help_text='Separate tags \
        with spaces, put quotes around multiple-word tags.')
    
    objects = QuerySetManager()
    
    class Meta(AbstractBaseResource.Meta):
        pass
    
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


class PersonOrganisation(models.Model):
    person = models.ForeignKey('contacts.Person',
        related_name='occupations')
    organisation = models.ForeignKey('contacts.Organisation',
        related_name='positions')
    title = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True,
        null=True)
    
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


class Person(Contact):
    user = models.OneToOneField('auth.User', related_name='contact',
        blank=True, null=True)
    title = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=75, db_index=True,
        blank=True, null=True)
    last_name = models.CharField(max_length=75, db_index=True,
        blank=True, null=True)
    suffix = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    organisations = models.ManyToManyField('contacts.Organisation',
        related_name='people', through='contacts.PersonOrganisation',
        blank=True, null=True)
    
    objects = QuerySetManager()
    
    class Meta(Contact.Meta):
        ordering = ['last_name', 'first_name']
        verbose_name_plural = 'people'
    
    def __unicode__(self):
        if self.first_name and self.last_name:
            return ', '.join([self.last_name, self.first_name])
        else:
            return self.name or 'Unnamed'
    
    @property
    def name(self):
        if self.first_name and self.last_name:
            return ' '.join([self.first_name, self.last_name])
        else:
            return self.first_name or self.last_name or None


class Organisation(Contact):
    name = models.CharField(max_length=150, db_index=True,
        blank=True, null=True)
    abn = models.CharField('ABN', max_length=11, db_index=True,
        blank=True, null=True)
    
    objects = QuerySetManager()
    
    class Meta(Contact.Meta):
        ordering = ['name']
    
    def __unicode__(self):
        return self.name

