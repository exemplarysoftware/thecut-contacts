# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from thecut.authorship.settings import AUTH_USER_MODEL


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Website.value'
        db.alter_column('contacts_website', 'value', self.gf('django.db.models.fields.URLField')(default='', max_length=255))

        # Changing field 'Website.name'
        db.alter_column('contacts_website', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Nickname.value'
        db.alter_column('contacts_nickname', 'value', self.gf('django.db.models.fields.CharField')(default='', max_length=75))

        # Changing field 'ContactGroup.tags'
        db.alter_column('contacts_contactgroup', 'tags', self.gf('tagging.fields.TagField')(default=''))

        # Changing field 'ContactGroup.notes'
        db.alter_column('contacts_contactgroup', 'notes', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'ContactGroup.name'
        db.alter_column('contacts_contactgroup', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=150))

        # Changing field 'Address.city'
        db.alter_column('contacts_address', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Address.street'
        db.alter_column('contacts_address', 'street', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Address.name'
        db.alter_column('contacts_address', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Address.country'
        db.alter_column('contacts_address', 'country', self.gf('django_countries.fields.CountryField')(max_length=2))

        # Changing field 'Address.state'
        db.alter_column('contacts_address', 'state', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Address.postcode'
        db.alter_column('contacts_address', 'postcode', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'PersonOrganisation.department'
        db.alter_column('contacts_personorganisation', 'department', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'PersonOrganisation.title'
        db.alter_column('contacts_personorganisation', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Contact.tags'
        db.alter_column('contacts_contact', 'tags', self.gf('tagging.fields.TagField')(default=''))

        # Changing field 'Contact.notes'
        db.alter_column('contacts_contact', 'notes', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Contact.biography'
        db.alter_column('contacts_contact', 'biography', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Email.value'
        db.alter_column('contacts_email', 'value', self.gf('django.db.models.fields.EmailField')(default='', max_length=75))

        # Changing field 'Email.name'
        db.alter_column('contacts_email', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Person.first_name'
        db.alter_column('contacts_person', 'first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=75))

        # Changing field 'Person.last_name'
        db.alter_column('contacts_person', 'last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=75))

        # Changing field 'Person.suffix'
        db.alter_column('contacts_person', 'suffix', self.gf('django.db.models.fields.CharField')(default='', max_length=15))

        # Changing field 'Person.title'
        db.alter_column('contacts_person', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=15))

        # Changing field 'Organisation.name'
        db.alter_column('contacts_organisation', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=150))

        # Changing field 'Organisation.abn'
        db.alter_column('contacts_organisation', 'abn', self.gf('django.db.models.fields.CharField')(default='', max_length=11))

        # Changing field 'InstantMessengerHandle.type'
        db.alter_column('contacts_instantmessengerhandle', 'type', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'InstantMessengerHandle.value'
        db.alter_column('contacts_instantmessengerhandle', 'value', self.gf('django.db.models.fields.CharField')(default='', max_length=75))

        # Changing field 'InstantMessengerHandle.name'
        db.alter_column('contacts_instantmessengerhandle', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Phone.type'
        db.alter_column('contacts_phone', 'type', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Phone.value'
        db.alter_column('contacts_phone', 'value', self.gf('django.db.models.fields.CharField')(default='', max_length=75))

        # Changing field 'Phone.name'
        db.alter_column('contacts_phone', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))


    def backwards(self, orm):

        # Changing field 'Website.value'
        db.alter_column('contacts_website', 'value', self.gf('django.db.models.fields.URLField')(max_length=255, null=True))

        # Changing field 'Website.name'
        db.alter_column('contacts_website', 'name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Nickname.value'
        db.alter_column('contacts_nickname', 'value', self.gf('django.db.models.fields.CharField')(max_length=75, null=True))

        # Changing field 'ContactGroup.tags'
        db.alter_column('contacts_contactgroup', 'tags', self.gf('tagging.fields.TagField')(null=True))

        # Changing field 'ContactGroup.notes'
        db.alter_column('contacts_contactgroup', 'notes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'ContactGroup.name'
        db.alter_column('contacts_contactgroup', 'name', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

        # Changing field 'Address.city'
        db.alter_column('contacts_address', 'city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Address.street'
        db.alter_column('contacts_address', 'street', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Address.name'
        db.alter_column('contacts_address', 'name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Address.country'
        db.alter_column('contacts_address', 'country', self.gf('django_countries.fields.CountryField')(max_length=2, null=True))

        # Changing field 'Address.state'
        db.alter_column('contacts_address', 'state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Address.postcode'
        db.alter_column('contacts_address', 'postcode', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'PersonOrganisation.department'
        db.alter_column('contacts_personorganisation', 'department', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'PersonOrganisation.title'
        db.alter_column('contacts_personorganisation', 'title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Contact.tags'
        db.alter_column('contacts_contact', 'tags', self.gf('tagging.fields.TagField')(null=True))

        # Changing field 'Contact.notes'
        db.alter_column('contacts_contact', 'notes', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Contact.biography'
        db.alter_column('contacts_contact', 'biography', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Email.value'
        db.alter_column('contacts_email', 'value', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True))

        # Changing field 'Email.name'
        db.alter_column('contacts_email', 'name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Person.first_name'
        db.alter_column('contacts_person', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=75, null=True))

        # Changing field 'Person.last_name'
        db.alter_column('contacts_person', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=75, null=True))

        # Changing field 'Person.suffix'
        db.alter_column('contacts_person', 'suffix', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'Person.title'
        db.alter_column('contacts_person', 'title', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'Organisation.name'
        db.alter_column('contacts_organisation', 'name', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

        # Changing field 'Organisation.abn'
        db.alter_column('contacts_organisation', 'abn', self.gf('django.db.models.fields.CharField')(max_length=11, null=True))

        # Changing field 'InstantMessengerHandle.type'
        db.alter_column('contacts_instantmessengerhandle', 'type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'InstantMessengerHandle.value'
        db.alter_column('contacts_instantmessengerhandle', 'value', self.gf('django.db.models.fields.CharField')(max_length=75, null=True))

        # Changing field 'InstantMessengerHandle.name'
        db.alter_column('contacts_instantmessengerhandle', 'name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Phone.type'
        db.alter_column('contacts_phone', 'type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Phone.value'
        db.alter_column('contacts_phone', 'value', self.gf('django.db.models.fields.CharField')(max_length=75, null=True))

        # Changing field 'Phone.name'
        db.alter_column('contacts_phone', 'name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))


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
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contacts.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'addresses'", 'to': "orm['contacts.Contact']"}),
            'country': ('django_countries.fields.CountryField', [], {'default': "u'AU'", 'max_length': '2', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'street': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'contacts.contact': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Contact'},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contact_created_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'contacts'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['contacts.ContactGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contact_publish_by_user'", 'null': 'True', 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'tags': ('tagging.fields.TagField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contact_updated_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)})
        },
        'contacts.contactgroup': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'ContactGroup'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contactgroup_created_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contactgroup_publish_by_user'", 'null': 'True', 'to': "orm['{0}']".format(AUTH_USER_MODEL)}),
            'tags': ('tagging.fields.TagField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contactgroup_updated_by_user'", 'to': "orm['{0}']".format(AUTH_USER_MODEL)})
        },
        'contacts.email': {
            'Meta': {'object_name': 'Email'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'emails'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'value': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'})
        },
        'contacts.instantmessengerhandle': {
            'Meta': {'object_name': 'InstantMessengerHandle'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'instant_messenger_handles'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'})
        },
        'contacts.nickname': {
            'Meta': {'object_name': 'Nickname'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'nicknames'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'})
        },
        'contacts.organisation': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Organisation', '_ormbases': ['contacts.Contact']},
            'abn': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '11', 'blank': 'True'}),
            'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'blank': 'True'})
        },
        'contacts.person': {
            'Meta': {'ordering': "[u'last_name', u'first_name']", 'object_name': 'Person', '_ormbases': ['contacts.Contact']},
            'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'}),
            'organisations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'people'", 'to': "orm['contacts.Organisation']", 'through': "orm['contacts.PersonOrganisation']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "u'contact'", 'unique': 'True', 'null': 'True', 'to': "orm['{0}']".format(AUTH_USER_MODEL)})
        },
        'contacts.personorganisation': {
            'Meta': {'object_name': 'PersonOrganisation'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'positions'", 'to': "orm['contacts.Organisation']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'occupations'", 'to': "orm['contacts.Person']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'contacts.phone': {
            'Meta': {'object_name': 'Phone'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'phones'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'blank': 'True'})
        },
        'contacts.website': {
            'Meta': {'object_name': 'Website'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'websites'", 'to': "orm['contacts.Contact']"}),
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
