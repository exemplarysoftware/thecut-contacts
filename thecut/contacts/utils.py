# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def python_2_unicode_compatible(class_):
    # Forwards compatibility with Django 1.5, taken from Django 1.4.5
    class_.__unicode__ = class_.__str__
    class_.__str__ = lambda self: self.__unicode__().encode('utf-8')
    return class_
