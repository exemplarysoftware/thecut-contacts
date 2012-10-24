# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings


DEFAULT_COUNTRY = getattr(settings, 'CONTACTS_DEFAULT_COUNTRY', 'AU')


INSTANT_MESSENGER_TYPES = getattr(settings, 'CONTACTS_INSTANT_MESSENGER_TYPES',
    ['AIM', 'Google Talk', 'ICQ', 'IRC', 'SIP', 'Skype', 'Windows Live',
    'XMPP', 'Yahoo!'])

PHONE_TYPES = getattr(settings, 'CONTACTS_PHONE_TYPES', ['Landline', 'Mobile',
    'Fax', 'VOIP'])

