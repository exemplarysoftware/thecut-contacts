# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models


class QuerySet(models.query.QuerySet):
    
    def get_first(self):
        """Return the first object in the QuerySet."""
        return self[:1].get()


class ActiveFeaturedQuerySet(QuerySet):
    
    def active(self):
        """Return active (enabled) objects."""
        return self.filter(is_enabled=True)
    
    def featured(self):
        """Return featured objects."""
        return self.filter(is_featured=True)

