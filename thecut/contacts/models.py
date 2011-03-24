from django.db import models
from django_countries import CountryField
from tagging.fields import TagField
from thecut.core.managers import QuerySetManager
from thecut.core.models import AbstractBaseResource


class Address(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, db_index=True,
        blank=True, null=True)
    state = models.CharField(max_length=50, db_index=True,
        blank=True, null=True)
    postcode = models.CharField(max_length=30, db_index=True,
        blank=True, null=True)
    country = CountryField(db_index=True, blank=True, null=True)
    
    def __unicode__(self):
        return self.address
    
    @property
    def address(self):
        return '%s %s %s %s %s' %(self.street, self.city,
            self.state, self.postcode, self.country)


class Email(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.EmailField(max_length=75, db_index=True,
        blank=True, null=True)
    
    def __unicode__(self):
        return self.value


class InstantMessengerHandle(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=75, db_index=True,
        blank=True, null=True)
    type = models.CharField(max_length=50, db_index=True,
        blank=True, null=True)
    
    def __unicode__(self):
        return self.value


class Nickname(models.Model):
    value = models.CharField(max_length=75, db_index=True,
        blank=True, null=True)
    
    def __unicode__(self):
        return self.value


class Phone(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=75, db_index=True,
        blank=True, null=True)
    type = models.CharField(max_length=50, db_index=True,
        blank=True, null=True)
    
    def __unicode__(self):
        return self.value


class Website(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.URLField(max_length=255, db_index=True,
        blank=True, null=True)
    
    def __unicode__(self):
        return self.value


class AbstractContact(AbstractBaseResource):
    nicknames = models.ManyToManyField('contacts.Nickname')
    addresses = models.ManyToManyField('contacts.Address',
        blank=True, null=True)
    phones = models.ManyToManyField('contacts.Phone')
    email_addresses = models.ManyToManyField('contacts.Email')
    instant_messenger_handles = models.ManyToManyField(
        'contacts.InstantMessengerHandle', blank=True, null=True)
    websites = models.ManyToManyField('contacts.Website',
        blank=True, null=True)
    image = models.FileField(
        upload_to='uploads/contacts/images/%Y/%m/%d',
        blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    tags = TagField(blank=True, null=True, help_text='Separate tags \
        with spaces, put quotes around multiple-word tags.')
    
    objects = QuerySetManager()
    
    class Meta:
        abstract = True


class Person(AbstractContact):
    title = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=75, db_index=True,
        blank=True, null=True)
    last_name = models.CharField(max_length=75, db_index=True,
        blank=True, null=True)
    suffix = models.CharField(max_length=15, blank=True, null=True)
    occupation = models.CharField(max_length=75, blank=True, null=True)
    organisations = models.ManyToManyField('contacts.Organisation',
        related_name='people', blank=True, null=True)
    
    objects = QuerySetManager()
    
    class Meta(AbstractContact.Meta):
        verbose_name_plural = 'people'
    
    def __unicode__(self):
        return self.name
    
    @property
    def name(self):
        return '%s %s' %(self.first_name, self.last_name)


class Organisation(AbstractContact):
    name = models.CharField(max_length=150, blank=True, null=True)
    abn = models.CharField('ABN', max_length=11, blank=True, null=True)
    
    objects = QuerySetManager()
    
    def __unicode__(self):
        return self.name

