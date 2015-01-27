# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max


def set_order(sender, instance, raw, contact_field='contact', **kwargs):
    if not raw and not instance.pk and not instance.order:
        filter_args = {contact_field: getattr(instance, contact_field)}
        order = instance.__class__.objects.filter(**filter_args).aggregate(
            order=Max('order')).get('order')
        instance.order = order + 1 if order is not None else 1


def set_personorganisation_order(*args, **kwargs):
    kwargs.setdefault('contact_field', 'person')
    set_order(*args, **kwargs)


def delete_image(sender, instance, **kwargs):
    """Deletes the image from the instance (without resaving the instance)."""
    from thecut.contacts.models import AbstractContact
    if isinstance(instance, AbstractContact):
        if instance.image:
            instance.image.delete(save=False)


def check_and_delete_image(sender, instance, raw, **kwargs):
    """If the image has changed for an instance, delete the 'old' image."""
    if not raw and instance.pk:
        from thecut.contacts.models import AbstractContact
        if isinstance(instance, AbstractContact):
            try:
                existing = sender.objects.get(pk=instance.pk)
            except sender.objects.DoesNotExist:
                pass
            else:
                if existing.image != instance.image:
                    delete_image(sender=sender, instance=existing)


def delete_related_detail(sender, instance, related_name):
    """Delete related contact detail if it is not linked to other contacts."""

    if settings.DELETE_RELATED_CONTACT_DETAILS:
        try:
            related_obj = getattr(instance, related_name)
        except ObjectDoesNotExist:
            pass
        else:
            query = {related_name: related_obj}
            if not sender.objects.filter(**query).exists():
                related_obj.delete()


def delete_related_address(sender, instance, **kwargs):
    return delete_related_detail(sender=sender, instance=instance,
                                 related_name='address')


def delete_related_email(sender, instance, **kwargs):
    return delete_related_detail(sender=sender, instance=instance,
                                 related_name='email')


def delete_related_instant_messenger_handle(sender, instance, **kwargs):
    return delete_related_detail(sender=sender, instance=instance,
                                 related_name='instant_messenger_handle')


def delete_related_nickname(sender, instance, **kwargs):
    return delete_related_detail(sender=sender, instance=instance,
                                 related_name='nickname')


def delete_related_phone(sender, instance, **kwargs):
    return delete_related_detail(sender=sender, instance=instance,
                                 related_name='phone')


def delete_related_website(sender, instance, **kwargs):
    return delete_related_detail(sender=sender, instance=instance,
                                 related_name='website')
