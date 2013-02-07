# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Person.last_name'
        db.delete_column(u'contacts_person', 'last_name')

        # Deleting field 'Person.first_name'
        db.delete_column(u'contacts_person', 'first_name')


    def backwards(self, orm):
        # Adding field 'Person.last_name'
        db.add_column(u'contacts_person', 'last_name',
                      self.gf('django.db.models.fields.CharField')(blank=True, default='', max_length=75, db_index=True),
                      keep_default=False)

        # Adding field 'Person.first_name'
        db.add_column(u'contacts_person', 'first_name',
                      self.gf('django.db.models.fields.CharField')(blank=True, default='', max_length=75, db_index=True),
                      keep_default=False)


    models = {
        u'accounts.account': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Account'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Account']"}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '254', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '254', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contacts.address': {
            'Meta': {'ordering': "[u'contact_addresses__order']", 'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'default': "u'AU'", 'max_length': '2', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'street': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'contacts.contact': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Contact'},
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': u"orm['contacts.Address']", 'through': u"orm['contacts.ContactAddress']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['accounts.User']"}),
            'emails': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': u"orm['contacts.Email']", 'through': u"orm['contacts.ContactEmail']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'contacts'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['contacts.ContactGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'instant_messenger_handles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': u"orm['contacts.InstantMessengerHandle']", 'through': u"orm['contacts.ContactInstantMessengerHandle']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nicknames': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': u"orm['contacts.Nickname']", 'through': u"orm['contacts.ContactNickname']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phones': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': u"orm['contacts.Phone']", 'through': u"orm['contacts.ContactPhone']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['accounts.User']"}),
            'websites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': u"orm['contacts.Website']", 'through': u"orm['contacts.ContactWebsite']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'})
        },
        u'contacts.contactaddress': {
            'Meta': {'ordering': "[u'order']", 'unique_together': "([u'contact', u'address'],)", 'object_name': 'ContactAddress'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_addresses'", 'to': u"orm['contacts.Address']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'contacts.contactemail': {
            'Meta': {'ordering': "[u'order']", 'unique_together': "([u'contact', u'email'],)", 'object_name': 'ContactEmail'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['contacts.Contact']"}),
            'email': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_emails'", 'to': u"orm['contacts.Email']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'contacts.contactgroup': {
            'Meta': {'ordering': "[u'name', u'-created_at']", 'object_name': 'ContactGroup'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['accounts.User']"})
        },
        u'contacts.contactinstantmessengerhandle': {
            'Meta': {'ordering': "[u'order']", 'unique_together': "([u'contact', u'instant_messenger_handle'],)", 'object_name': 'ContactInstantMessengerHandle'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instant_messenger_handle': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_instant_messenger_handles'", 'to': u"orm['contacts.InstantMessengerHandle']"}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'contacts.contactnickname': {
            'Meta': {'ordering': "[u'order']", 'unique_together': "([u'contact', u'nickname'],)", 'object_name': 'ContactNickname'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_nicknames'", 'to': u"orm['contacts.Nickname']"}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'contacts.contactphone': {
            'Meta': {'ordering': "[u'order']", 'unique_together': "([u'contact', u'phone'],)", 'object_name': 'ContactPhone'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'phone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_phones'", 'to': u"orm['contacts.Phone']"})
        },
        u'contacts.contactwebsite': {
            'Meta': {'ordering': "[u'order']", 'unique_together': "([u'contact', u'website'],)", 'object_name': 'ContactWebsite'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_websites'", 'to': u"orm['contacts.Website']"})
        },
        u'contacts.email': {
            'Meta': {'ordering': "[u'contact_emails__order']", 'object_name': 'Email'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'value': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'})
        },
        u'contacts.instantmessengerhandle': {
            'Meta': {'ordering': "[u'contact_instant_messenger_handles__order']", 'object_name': 'InstantMessengerHandle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'})
        },
        u'contacts.nickname': {
            'Meta': {'ordering': "[u'contact_nicknames__order']", 'object_name': 'Nickname'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'})
        },
        u'contacts.organisation': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Organisation'},
            'abn': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '11', 'blank': 'True'}),
            u'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'})
        },
        u'contacts.person': {
            'Meta': {'ordering': "[u'short_name']", 'object_name': 'Person'},
            u'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1', 'blank': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'blank': 'True'}),
            'organisations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'people'", 'to': u"orm['contacts.Organisation']", 'through': u"orm['contacts.PersonOrganisation']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "u'contact'", 'unique': 'True', 'null': 'True', 'to': u"orm['accounts.User']"})
        },
        u'contacts.personorganisation': {
            'Meta': {'object_name': 'PersonOrganisation'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'positions'", 'to': u"orm['contacts.Organisation']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'occupations'", 'to': u"orm['contacts.Person']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'contacts.phone': {
            'Meta': {'ordering': "[u'contact_phones__order']", 'object_name': 'Phone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'})
        },
        u'contacts.website': {
            'Meta': {'ordering': "[u'contact_websites__order']", 'object_name': 'Website'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'value': ('django.db.models.fields.URLField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['contacts']