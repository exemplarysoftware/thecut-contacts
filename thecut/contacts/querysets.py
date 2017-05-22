# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models


class ActiveFeaturedQuerySet(models.query.QuerySet):

    def active(self):
        """Return active (enabled) objects."""
        return self.filter(is_enabled=True)

    def featured(self):
        """Return featured objects."""
        return self.filter(is_featured=True)
