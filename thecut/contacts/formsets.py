# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.forms.models import BaseInlineFormSet


class ContactRelatedInlineFormSet(BaseInlineFormSet):
    """InlineFormSet which will also delete a custom related object."""
    
    _related_name = None
    
    def save_existing_objects(self, *args, **kwargs):
        saved_instances = super(ContactRelatedInlineFormSet,
            self).save_existing_objects(*args, **kwargs)
        for obj in self.deleted_objects:
            related_obj = getattr(obj, self._related_name)
            # Only delete related object if it is not linked to something else.
            query = {'%s' %(self._related_name): related_obj}
            if not obj.__class__.objects.filter(**query).exists():
                related_obj.delete()
        return saved_instances


class ContactAddressInlineFormSet(ContactRelatedInlineFormSet):
    
    _related_name = 'address'


class ContactEmailInlineFormSet(ContactRelatedInlineFormSet):
    
    _related_name = 'email'


class ContactInstantMessengerHandleInlineFormSet(ContactRelatedInlineFormSet):
    
    _related_name = 'instant_messenger_handle'


class ContactNicknameInlineFormSet(ContactRelatedInlineFormSet):
    
    _related_name = 'nickname'


class ContactPhoneInlineFormSet(ContactRelatedInlineFormSet):
    
    _related_name = 'phone'


class ContactWebsiteInlineFormSet(ContactRelatedInlineFormSet):
    
    _related_name = 'website'

