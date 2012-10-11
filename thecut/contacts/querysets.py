# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models


class QuerySet(models.query.QuerySet):
    
    def active(self):
        """Return active (enabled) objects."""
        return self.filter(is_enabled=True)
    
    def featured(self):
        """Return featured objects."""
        return self.filter(is_featured=True)


class AbstractContactGroupQuerySet(QuerySet):
    pass


class AbstractContactQuerySet(QuerySet):
    pass


class ContactAddressQuerySet(models.query.QuerySet):
    
    def addresses(self):
        """Return ordered QuerySet of related ``Address`` objects.
        
        :returns: Filtered QuerySet.
        :rtype: QuerySet instance.
        
        """
        from thecut.contacts.models import Address
        return Address.objects.filter(contacts__in=self).order_by(
            'contacts__order')
    
    def contacts(self):
        """Return related ``Contact`` objects.
        
        :returns: Filtered AbstractContactQuerySet.
        :rtype: AbstractContactQuerySet instance.
        
        """
        from thecut.contacts.models import Contact
        return Contact.objects.filter(addresses__in=self)
    
    def get_first(self):
        """Return the first ``Address`` object.
        
        :returns: First Address object.
        :rtype: Address instance or None.
        
        """
        queryset = self.order_by('order')[:1]
        return queryset[0].address if queryset else None


class ContactEmailQuerySet(models.query.QuerySet):
    
    def emails(self):
        """Return ordered QuerySet of related ``Email`` objects.
        
        :returns: Filtered QuerySet.
        :rtype: QuerySet instance.
        
        """
        from thecut.contacts.models import Email
        return Email.objects.filter(contacts__in=self).order_by(
            'contacts__order')
    
    def contacts(self):
        """Return related ``Contact`` objects.
        
        :returns: Filtered AbstractContactQuerySet.
        :rtype: AbstractContactQuerySet instance.
        
        """
        from thecut.contacts.models import Contact
        return Contact.objects.filter(emails__in=self)
    
    def get_first(self):
        """Return the first ``Email`` object.
        
        :returns: First Email object.
        :rtype: Email instance or None.
        
        """
        queryset = self.order_by('order')[:1]
        return queryset[0].email if queryset else None


class ContactInstantMessengerHandleQuerySet(models.query.QuerySet):
    
    def instant_messenger_handles(self):
        """Return ordered QuerySet of related ``InstantMessengerHandle`` objects.
        
        :returns: Filtered QuerySet.
        :rtype: QuerySet instance.
        
        """
        from thecut.contacts.models import InstantMessengerHandle
        return InstantMessengerHandle.objects.filter(
            contacts__in=self).order_by('contacts__order')
    
    def contacts(self):
        """Return related ``Contact`` objects.
        
        :returns: Filtered AbstractContactQuerySet.
        :rtype: AbstractContactQuerySet instance.
        
        """
        from thecut.contacts.models import Contact
        return Contact.objects.filter(instant_messenger_handles__in=self)
    
    def get_first(self):
        """Return the first ``InstantMessengerHandle`` object.
        
        :returns: First InstantMessengerHandle object.
        :rtype: InstantMessengerHandle instance or None.
        
        """
        queryset = self.order_by('order')[:1]
        return queryset[0].instant_messenger_handle if queryset else None


class ContactNicknameQuerySet(models.query.QuerySet):
    
    def nicknames(self):
        """Return ordered QuerySet of related ``Nickname`` objects.
        
        :returns: Filtered QuerySet.
        :rtype: QuerySet instance.
        
        """
        from thecut.contacts.models import Nickname
        return Nickname.objects.filter(contacts__in=self).order_by(
            'contacts__order')
    
    def contacts(self):
        """Return related ``Contact`` objects.
        
        :returns: Filtered AbstractContactQuerySet.
        :rtype: AbstractContactQuerySet instance.
        
        """
        from thecut.contacts.models import Contact
        return Contact.objects.filter(nicknames__in=self)
    
    def get_first(self):
        """Return the first ``Nickname`` object.
        
        :returns: First Nickname object.
        :rtype: Nickname instance or None.
        
        """
        queryset = self.order_by('order')[:1]
        return queryset[0].nickname if queryset else None


class ContactPhoneQuerySet(models.query.QuerySet):
    
    def phones(self):
        """Return ordered QuerySet of related ``Phone`` objects.
        
        :returns: Filtered QuerySet.
        :rtype: QuerySet instance.
        
        """
        from thecut.contacts.models import Phone
        return Phone.objects.filter(contacts__in=self).order_by(
            'contacts__order')
    
    def contacts(self):
        """Return related ``Contact`` objects.
        
        :returns: Filtered AbstractContactQuerySet.
        :rtype: AbstractContactQuerySet instance.
        
        """
        from thecut.contacts.models import Contact
        return Contact.objects.filter(phones__in=self)
    
    def get_first(self):
        """Return the first ``Phone`` object.
        
        :returns: First Phone object.
        :rtype: Phone instance or None.
        
        """
        queryset = self.order_by('order')[:1]
        return queryset[0].phone if queryset else None


class ContactWebsiteQuerySet(models.query.QuerySet):
    
    def websites(self):
        """Return ordered QuerySet of related ``Website`` objects.
        
        :returns: Filtered QuerySet.
        :rtype: QuerySet instance.
        
        """
        from thecut.contacts.models import Website
        return Website.objects.filter(contacts__in=self).order_by(
            'contacts__order')
    
    def contacts(self):
        """Return related ``Contact`` objects.
        
        :returns: Filtered AbstractContactQuerySet.
        :rtype: AbstractContactQuerySet instance.
        
        """
        from thecut.contacts.models import Contact
        return Contact.objects.filter(websites__in=self)
    
    def get_first(self):
        """Return the first ``Website`` object.
        
        :returns: First Website object.
        :rtype: Website instance or None.
        
        """
        queryset = self.order_by('order')[:1]
        return queryset[0].website if queryset else None

