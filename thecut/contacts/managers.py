# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.gis.db import models
from model_utils.managers import PassThroughManagerMixin


class AddressManager(PassThroughManagerMixin, models.GeoManager):

    pass
