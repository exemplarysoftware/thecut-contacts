# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ContactGroup'
        db.create_table('contacts_contactgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('publish_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('expire_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('publish_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contactgroup_publish_by_user', null=True, to=orm['auth.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contactgroup_created_by_user', to=orm['auth.User'])),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contactgroup_updated_by_user', to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=150, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')(null=True)),
        ))
        db.send_create_signal('contacts', ['ContactGroup'])

        # Adding M2M table for field groups on 'Contact'
        db.create_table('contacts_contact_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contact', models.ForeignKey(orm['contacts.contact'], null=False)),
            ('contactgroup', models.ForeignKey(orm['contacts.contactgroup'], null=False))
        ))
        db.create_unique('contacts_contact_groups', ['contact_id', 'contactgroup_id'])


    def backwards(self, orm):
        
        # Deleting model 'ContactGroup'
        db.delete_table('contacts_contactgroup')

        # Removing M2M table for field groups on 'Contact'
        db.delete_table('contacts_contact_groups')


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
            'city': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'addresses'", 'to': "orm['contacts.Contact']"}),
            'country': ('django_countries.fields.CountryField', [], {'default': "'AU'", 'max_length': '2', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'contacts.contact': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Contact'},
            'biography': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contact_created_by_user'", 'to': "orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'contacts'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['contacts.ContactGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contact_publish_by_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contact_updated_by_user'", 'to': "orm['auth.User']"})
        },
        'contacts.contactgroup': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'ContactGroup'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contactgroup_created_by_user'", 'to': "orm['auth.User']"}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contactgroup_publish_by_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contactgroup_updated_by_user'", 'to': "orm['auth.User']"})
        },
        'contacts.email': {
            'Meta': {'object_name': 'Email'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'emails'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'})
        },
        'contacts.instantmessengerhandle': {
            'Meta': {'object_name': 'InstantMessengerHandle'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instant_messenger_handles'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'})
        },
        'contacts.nickname': {
            'Meta': {'object_name': 'Nickname'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'nicknames'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'})
        },
        'contacts.organisation': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Organisation', '_ormbases': ['contacts.Contact']},
            'abn': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '150', 'null': 'True', 'blank': 'True'})
        },
        'contacts.person': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Person', '_ormbases': ['contacts.Contact']},
            'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'organisations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'people'", 'to': "orm['contacts.Organisation']", 'through': "orm['contacts.PersonOrganisation']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'contact'", 'unique': 'True', 'null': 'True', 'to': "orm['auth.User']"})
        },
        'contacts.personorganisation': {
            'Meta': {'object_name': 'PersonOrganisation'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Organisation']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Person']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'contacts.phone': {
            'Meta': {'object_name': 'Phone'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phones'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'})
        },
        'contacts.website': {
            'Meta': {'object_name': 'Website'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'websites'", 'to': "orm['contacts.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.URLField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'})
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
