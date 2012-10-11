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

