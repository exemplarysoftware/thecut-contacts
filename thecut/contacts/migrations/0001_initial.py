# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Address'
        db.create_table('contacts_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=30, null=True, blank=True)),
            ('country', self.gf('django_countries.fields.CountryField')(db_index=True, max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal('contacts', ['Address'])

        # Adding model 'Email'
        db.create_table('contacts_email', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.EmailField')(db_index=True, max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('contacts', ['Email'])

        # Adding model 'InstantMessengerHandle'
        db.create_table('contacts_instantmessengerhandle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=75, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('contacts', ['InstantMessengerHandle'])

        # Adding model 'Nickname'
        db.create_table('contacts_nickname', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('contacts', ['Nickname'])

        # Adding model 'Phone'
        db.create_table('contacts_phone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=75, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('contacts', ['Phone'])

        # Adding model 'Website'
        db.create_table('contacts_website', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.URLField')(db_index=True, max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('contacts', ['Website'])

        # Adding model 'Person'
        db.create_table('contacts_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('publish_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('expire_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('publish_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='person_publish_by_user', null=True, to=orm['auth.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='person_created_by_user', to=orm['auth.User'])),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='person_updated_by_user', to=orm['auth.User'])),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('biography', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=75, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=75, null=True, blank=True)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('contacts', ['Person'])

        # Adding M2M table for field nicknames on 'Person'
        db.create_table('contacts_person_nicknames', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['contacts.person'], null=False)),
            ('nickname', models.ForeignKey(orm['contacts.nickname'], null=False))
        ))
        db.create_unique('contacts_person_nicknames', ['person_id', 'nickname_id'])

        # Adding M2M table for field addresses on 'Person'
        db.create_table('contacts_person_addresses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['contacts.person'], null=False)),
            ('address', models.ForeignKey(orm['contacts.address'], null=False))
        ))
        db.create_unique('contacts_person_addresses', ['person_id', 'address_id'])

        # Adding M2M table for field phones on 'Person'
        db.create_table('contacts_person_phones', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['contacts.person'], null=False)),
            ('phone', models.ForeignKey(orm['contacts.phone'], null=False))
        ))
        db.create_unique('contacts_person_phones', ['person_id', 'phone_id'])

        # Adding M2M table for field email_addresses on 'Person'
        db.create_table('contacts_person_email_addresses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['contacts.person'], null=False)),
            ('email', models.ForeignKey(orm['contacts.email'], null=False))
        ))
        db.create_unique('contacts_person_email_addresses', ['person_id', 'email_id'])

        # Adding M2M table for field instant_messenger_handles on 'Person'
        db.create_table('contacts_person_instant_messenger_handles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['contacts.person'], null=False)),
            ('instantmessengerhandle', models.ForeignKey(orm['contacts.instantmessengerhandle'], null=False))
        ))
        db.create_unique('contacts_person_instant_messenger_handles', ['person_id', 'instantmessengerhandle_id'])

        # Adding M2M table for field websites on 'Person'
        db.create_table('contacts_person_websites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['contacts.person'], null=False)),
            ('website', models.ForeignKey(orm['contacts.website'], null=False))
        ))
        db.create_unique('contacts_person_websites', ['person_id', 'website_id'])

        # Adding model 'Organisation'
        db.create_table('contacts_organisation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('publish_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('expire_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('publish_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='organisation_publish_by_user', null=True, to=orm['auth.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='organisation_created_by_user', to=orm['auth.User'])),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='organisation_updated_by_user', to=orm['auth.User'])),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('biography', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('abn', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
        ))
        db.send_create_signal('contacts', ['Organisation'])

        # Adding M2M table for field nicknames on 'Organisation'
        db.create_table('contacts_organisation_nicknames', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organisation', models.ForeignKey(orm['contacts.organisation'], null=False)),
            ('nickname', models.ForeignKey(orm['contacts.nickname'], null=False))
        ))
        db.create_unique('contacts_organisation_nicknames', ['organisation_id', 'nickname_id'])

        # Adding M2M table for field addresses on 'Organisation'
        db.create_table('contacts_organisation_addresses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organisation', models.ForeignKey(orm['contacts.organisation'], null=False)),
            ('address', models.ForeignKey(orm['contacts.address'], null=False))
        ))
        db.create_unique('contacts_organisation_addresses', ['organisation_id', 'address_id'])

        # Adding M2M table for field phones on 'Organisation'
        db.create_table('contacts_organisation_phones', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organisation', models.ForeignKey(orm['contacts.organisation'], null=False)),
            ('phone', models.ForeignKey(orm['contacts.phone'], null=False))
        ))
        db.create_unique('contacts_organisation_phones', ['organisation_id', 'phone_id'])

        # Adding M2M table for field email_addresses on 'Organisation'
        db.create_table('contacts_organisation_email_addresses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organisation', models.ForeignKey(orm['contacts.organisation'], null=False)),
            ('email', models.ForeignKey(orm['contacts.email'], null=False))
        ))
        db.create_unique('contacts_organisation_email_addresses', ['organisation_id', 'email_id'])

        # Adding M2M table for field instant_messenger_handles on 'Organisation'
        db.create_table('contacts_organisation_instant_messenger_handles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organisation', models.ForeignKey(orm['contacts.organisation'], null=False)),
            ('instantmessengerhandle', models.ForeignKey(orm['contacts.instantmessengerhandle'], null=False))
        ))
        db.create_unique('contacts_organisation_instant_messenger_handles', ['organisation_id', 'instantmessengerhandle_id'])

        # Adding M2M table for field websites on 'Organisation'
        db.create_table('contacts_organisation_websites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organisation', models.ForeignKey(orm['contacts.organisation'], null=False)),
            ('website', models.ForeignKey(orm['contacts.website'], null=False))
        ))
        db.create_unique('contacts_organisation_websites', ['organisation_id', 'website_id'])


    def backwards(self, orm):
        
        # Deleting model 'Address'
        db.delete_table('contacts_address')

        # Deleting model 'Email'
        db.delete_table('contacts_email')

        # Deleting model 'InstantMessengerHandle'
        db.delete_table('contacts_instantmessengerhandle')

        # Deleting model 'Nickname'
        db.delete_table('contacts_nickname')

        # Deleting model 'Phone'
        db.delete_table('contacts_phone')

        # Deleting model 'Website'
        db.delete_table('contacts_website')

        # Deleting model 'Person'
        db.delete_table('contacts_person')

        # Removing M2M table for field nicknames on 'Person'
        db.delete_table('contacts_person_nicknames')

        # Removing M2M table for field addresses on 'Person'
        db.delete_table('contacts_person_addresses')

        # Removing M2M table for field phones on 'Person'
        db.delete_table('contacts_person_phones')

        # Removing M2M table for field email_addresses on 'Person'
        db.delete_table('contacts_person_email_addresses')

        # Removing M2M table for field instant_messenger_handles on 'Person'
        db.delete_table('contacts_person_instant_messenger_handles')

        # Removing M2M table for field websites on 'Person'
        db.delete_table('contacts_person_websites')

        # Deleting model 'Organisation'
        db.delete_table('contacts_organisation')

        # Removing M2M table for field nicknames on 'Organisation'
        db.delete_table('contacts_organisation_nicknames')

        # Removing M2M table for field addresses on 'Organisation'
        db.delete_table('contacts_organisation_addresses')

        # Removing M2M table for field phones on 'Organisation'
        db.delete_table('contacts_organisation_phones')

        # Removing M2M table for field email_addresses on 'Organisation'
        db.delete_table('contacts_organisation_email_addresses')

        # Removing M2M table for field instant_messenger_handles on 'Organisation'
        db.delete_table('contacts_organisation_instant_messenger_handles')

        # Removing M2M table for field websites on 'Organisation'
        db.delete_table('contacts_organisation_websites')


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
            'country': ('django_countries.fields.CountryField', [], {'db_index': 'True', 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'contacts.email': {
            'Meta': {'object_name': 'Email'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'})
        },
        'contacts.instantmessengerhandle': {
            'Meta': {'object_name': 'InstantMessengerHandle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'})
        },
        'contacts.nickname': {
            'Meta': {'object_name': 'Nickname'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'})
        },
        'contacts.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'abn': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['contacts.Address']", 'null': 'True', 'blank': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'organisation_created_by_user'", 'to': "orm['auth.User']"}),
            'email_addresses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts.Email']", 'symmetrical': 'False'}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'instant_messenger_handles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['contacts.InstantMessengerHandle']", 'null': 'True', 'blank': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'nicknames': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts.Nickname']", 'symmetrical': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phones': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts.Phone']", 'symmetrical': 'False'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'organisation_publish_by_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'tags': ('tagging.fields.TagField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'organisation_updated_by_user'", 'to': "orm['auth.User']"}),
            'websites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['contacts.Website']", 'null': 'True', 'blank': 'True'})
        },
        'contacts.person': {
            'Meta': {'object_name': 'Person'},
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['contacts.Address']", 'null': 'True', 'blank': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person_created_by_user'", 'to': "orm['auth.User']"}),
            'email_addresses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts.Email']", 'symmetrical': 'False'}),
            'expire_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'instant_messenger_handles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['contacts.InstantMessengerHandle']", 'null': 'True', 'blank': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'nicknames': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts.Nickname']", 'symmetrical': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'phones': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts.Phone']", 'symmetrical': 'False'}),
            'publish_at': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'person_publish_by_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person_updated_by_user'", 'to': "orm['auth.User']"}),
            'websites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['contacts.Website']", 'null': 'True', 'blank': 'True'})
        },
        'contacts.phone': {
            'Meta': {'object_name': 'Phone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'})
        },
        'contacts.website': {
            'Meta': {'object_name': 'Website'},
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
