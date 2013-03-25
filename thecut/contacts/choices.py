# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from thecut.contacts import settings


MALE = 'M'
FEMALE = 'F'
GENDERS = [(MALE, 'Male'), (FEMALE, 'Female')]

INSTANT_MESSENGER_TYPES = [(value, value) for value in
                           settings.INSTANT_MESSENGER_TYPES]

PHONE_TYPES = [(value, value) for value in settings.PHONE_TYPES]
