# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from thecut.contacts.models import ContactGroup
import factory
from django.contrib.auth.models import User


class UserFactory(factory.Factory):
    FACTORY_FOR = User
    username = factory.Sequence(lambda n: 'user_%s' % n)


class ContactGroupFactory(factory.Factory):
    FACTORY_FOR = ContactGroup
    created_by = factory.SubFactory(UserFactory)
    updated_by = factory.SubFactory(UserFactory)


class TestQuerySet(TestCase):

    def setUp(self):
        self.first_group = ContactGroupFactory()
        self.first_group.save()
        self.second_group = ContactGroupFactory()
        self.second_group.save()

    def test_get_first_returns_first_object_in_queryset(self):
        groups = ContactGroup.objects.all()
        result = ContactGroup.objects.get_first()

        self.assertIn(result, groups)
        self.assertEqual(result, groups[0])

    def test_get_first_raises_exception_when_no_objects_exist(self):
        self.first_group.delete()
        self.second_group.delete()

        self.assertRaises(ContactGroup.DoesNotExist,
                          ContactGroup.objects.get_first)

    def test_active_returns_only_enabled_objects(self):
        self.first_group.is_enabled = True
        self.first_group.save()
        self.second_group.is_enabled = False
        self.second_group.save()

        queryset = ContactGroup.objects.active()

        self.assertEqual(queryset.count(), 1)
        self.assertIn(self.first_group, queryset)
        self.assertNotIn(self.second_group, queryset)

    def test_featured_returns_only_featured_objects(self):
        self.first_group.is_featured = True
        self.first_group.save()
        self.second_group.is_featured = False
        self.second_group.save()

        queryset = ContactGroup.objects.featured()

        self.assertEqual(queryset.count(), 1)
        self.assertIn(self.first_group, queryset)
        self.assertNotIn(self.second_group, queryset)
