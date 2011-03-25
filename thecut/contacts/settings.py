from django.conf import settings


DEFAULT_COUNTRY = getattr(settings, 'CONTACTS_DEFAULT_COUNTRY', 'AU')


INSTANT_MESSENGER_TYPE_LIST = [
    'AIM',
    'Google Talk',
    'ICQ',
    'IRC',
    'SIP',
    'Skype',
    'Windows Live',
    'XMPP',
    'Yahoo!',
]

INSTANT_MESSENGER_TYPES = [(value, value) for value in
    INSTANT_MESSENGER_TYPE_LIST]


PHONE_TYPE_LIST = [
    'Landline',
    'Mobile',
    'Fax',
    'VOIP',
]

PHONE_TYPES = [(value, value) for value in PHONE_TYPE_LIST]

