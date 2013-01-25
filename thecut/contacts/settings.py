# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


DEFAULT_COUNTRY = getattr(settings, 'CONTACTS_DEFAULT_COUNTRY', 'AU')


INSTANT_MESSENGER_TYPES = getattr(settings, 'CONTACTS_INSTANT_MESSENGER_TYPES',
    ['AIM', 'Google Talk', 'ICQ', 'IRC', 'SIP', 'Skype', 'Windows Live',
    'XMPP', 'Yahoo!'])

PHONE_TYPES = getattr(settings, 'CONTACTS_PHONE_TYPES', ['Landline', 'Mobile',
    'Fax', 'VOIP'])

DELETE_RELATED_CONTACT_DETAILS = getattr(settings,
    'CONTACTS_DELETE_RELATED_CONTACT_DETAILS', True)
