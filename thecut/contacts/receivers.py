# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db.models import Max
from django.dispatch import receiver


def set_order(sender, instance, raw, *args, **kwargs):
    if not raw and not instance.pk and not instance.order:
        order = instance.__class__.objects.filter(
            contact=instance.contact).aggregate(order=Max('order')).get('order')
        instance.order = order + 1 if order is not None else 1

