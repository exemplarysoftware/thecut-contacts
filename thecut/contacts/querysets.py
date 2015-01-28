# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.gis.db.models.query import GeoQuerySet
from django.db import models
import warnings


class DeprecatedQuerySetMixin(object):

    def get_first(self):
        """Deprecated - instead use 'first()'."""
        # Pre Django 1.6 compatibility
        warnings.warn('\'get_first\' method is deprecated - use \'first()\' '
                      'method.', DeprecationWarning, stacklevel=2)
        return self[:1].get()


class QuerySet(DeprecatedQuerySetMixin, models.query.QuerySet):

    pass


class GeoQuerySet(DeprecatedQuerySetMixin, GeoQuerySet):

    pass


class ActiveFeaturedQuerySet(QuerySet):

    def active(self):
        """Return active (enabled) objects."""
        return self.filter(is_enabled=True)

    def featured(self):
        """Return featured objects."""
        return self.filter(is_featured=True)
