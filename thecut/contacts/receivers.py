# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db.models import Max
from django.dispatch import receiver


def set_order(sender, instance, raw, contact_field='contact', **kwargs):
    if not raw and not instance.pk and not instance.order:
        filter_args = {contact_field: getattr(instance, contact_field)}
        order = instance.__class__.objects.filter(**filter_args).aggregate(
            order=Max('order')).get('order')
        instance.order = order + 1 if order is not None else 1


def set_personorganisation_order(*args, **kwargs):
    kwargs.setdefault('contact_field', 'person')
    set_order(*args, **kwargs)

