# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from thecut.authorship.settings import AUTH_USER_MODEL


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.gender'
        db.add_column('contacts_person', 'gender',
                      self.gf('django.db.models.fields.CharField')(default=u'', max_length=1, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.gender'
        db.delete_column('contacts_person', 'gender')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        AUTH_USER_MODEL: {
            'Meta': {'object_name': AUTH_USER_MODEL.split('.')[-1]},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contacts.address': {
            'Meta': {'ordering': "[u'contact_addresses__order']", 'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'default': "u'AU'", 'max_length': '2', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'street': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'contacts.contact': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Contact'},
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': "orm['contacts.Address']", 'through': "orm['contacts.ContactAddress']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'emails': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': "orm['contacts.Email']", 'through': "orm['contacts.ContactEmail']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'contacts'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['contacts.ContactGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'instant_messenger_handles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': "orm['contacts.InstantMessengerHandle']", 'through': "orm['contacts.ContactInstantMessengerHandle']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nicknames': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': "orm['contacts.Nickname']", 'through': "orm['contacts.ContactNickname']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phones': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': "orm['contacts.Phone']", 'through': "orm['contacts.ContactPhone']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'websites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': "orm['contacts.Website']", 'through': "orm['contacts.ContactWebsite']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'})
        },
        'contacts.contactaddress': {
            'Meta': {'ordering': "[u'order']", 'unique_together': "([u'contact', u'address'],)", 'object_name': 'ContactAddress'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_addresses'", 'to': "orm['contacts.Address']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'contacts.contactemail': {
            'Meta': {'ordering': "[u'order']", 'unique_together': "([u'contact', u'email'],)", 'object_name': 'ContactEmail'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': "orm['contacts.Contact']"}),
            'email': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_emails'", 'to': "orm['contacts.Email']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'contacts.contactgroup': {
            'Meta': {'ordering': "[u'name', u'-created_at']", 'object_name': 'ContactGroup'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)})
        },
        'contacts.contactinstantmessengerhandle': {
            'Meta': {'ordering': "[u'order']", 'unique_together': "([u'contact', u'instant_messenger_handle'],)", 'object_name': 'ContactInstantMessengerHandle'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instant_messenger_handle': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_instant_messenger_handles'", 'to': "orm['contacts.InstantMessengerHandle']"}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'contacts.contactnickname': {
            'Meta': {'ordering': "[u'order']", 'unique_together': "([u'contact', u'nickname'],)", 'object_name': 'ContactNickname'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_nicknames'", 'to': "orm['contacts.Nickname']"}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'contacts.contactphone': {
            'Meta': {'ordering': "[u'order']", 'unique_together': "([u'contact', u'phone'],)", 'object_name': 'ContactPhone'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'phone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_phones'", 'to': "orm['contacts.Phone']"})
        },
        'contacts.contactwebsite': {
            'Meta': {'ordering': "[u'order']", 'unique_together': "([u'contact', u'website'],)", 'object_name': 'ContactWebsite'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_websites'", 'to': "orm['contacts.Website']"})
        },
        'contacts.email': {
            'Meta': {'ordering': "[u'contact_emails__order']", 'object_name': 'Email'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'value': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'})
        },
        'contacts.instantmessengerhandle': {
            'Meta': {'ordering': "[u'contact_instant_messenger_handles__order']", 'object_name': 'InstantMessengerHandle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'})
        },
        'contacts.nickname': {
            'Meta': {'ordering': "[u'contact_nicknames__order']", 'object_name': 'Nickname'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'})
        },
        'contacts.organisation': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Organisation'},
            'abn': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '11', 'blank': 'True'}),
            'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'})
        },
        'contacts.person': {
            'Meta': {'ordering': "[u'last_name', u'first_name']", 'object_name': 'Person'},
            'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'}),
            'organisations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'people'", 'to': "orm['contacts.Organisation']", 'through': "orm['contacts.PersonOrganisation']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "u'contact'", 'unique': 'True', 'null': 'True', 'to': "orm['{0}']".format(AUTH_USER_MODEL)})
        },
        'contacts.personorganisation': {
            'Meta': {'object_name': 'PersonOrganisation'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'positions'", 'to': "orm['contacts.Organisation']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'occupations'", 'to': "orm['contacts.Person']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'contacts.phone': {
            'Meta': {'ordering': "[u'contact_phones__order']", 'object_name': 'Phone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'})
        },
        'contacts.website': {
            'Meta': {'ordering': "[u'contact_websites__order']", 'object_name': 'Website'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'value': ('django.db.models.fields.URLField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contacts']
