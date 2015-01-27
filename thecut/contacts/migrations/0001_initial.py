# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields
import django.contrib.gis.db.models.fields
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, blank=True)),
                ('street', models.TextField(blank=True)),
                ('city', models.CharField(db_index=True, max_length=250, blank=True)),
                ('state', models.CharField(db_index=True, max_length=250, blank=True)),
                ('postcode', models.CharField(db_index=True, max_length=50, blank=True)),
                ('country', django_countries.fields.CountryField(default='AU', max_length=2, db_index=True, blank=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
            ],
            options={
                'ordering': ['contact_addresses__order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(null=True, upload_to='uploads/contacts/images/%Y/%m/%d', blank=True)),
                ('biography', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('is_featured', models.BooleanField(default=False, verbose_name='featured')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
                'get_latest_by': 'created_at',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('address', models.ForeignKey(related_name='contact_addresses', to='contacts.Address')),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=250, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('is_featured', models.BooleanField(default=False, verbose_name='featured')),
                ('created_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('updated_by', models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name', '-created_at'),
                'abstract': False,
                'get_latest_by': 'created_at',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactInstantMessengerHandle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactNickname',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactPhone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactWebsite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, blank=True)),
                ('value', models.EmailField(db_index=True, max_length=254, verbose_name='Email', blank=True)),
            ],
            options={
                'ordering': ['contact_emails__order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstantMessengerHandle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, blank=True)),
                ('value', models.CharField(db_index=True, max_length=254, verbose_name='ID', blank=True)),
                ('type', models.CharField(blank=True, max_length=50, db_index=True, choices=[('AIM', 'AIM'), ('Google Talk', 'Google Talk'), ('ICQ', 'ICQ'), ('IRC', 'IRC'), ('SIP', 'SIP'), ('Skype', 'Skype'), ('Windows Live', 'Windows Live'), ('XMPP', 'XMPP'), ('Yahoo!', 'Yahoo!')])),
            ],
            options={
                'ordering': ['contact_instant_messenger_handles__order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nickname',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(db_index=True, max_length=250, verbose_name='Name', blank=True)),
            ],
            options={
                'ordering': ['contact_nicknames__order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('contact_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='contacts.Contact')),
                ('name', models.CharField(db_index=True, max_length=250, blank=True)),
                ('abn', models.CharField(db_index=True, max_length=11, verbose_name='ABN', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'get_latest_by': 'created_at',
            },
            bases=('contacts.contact',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('contact_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='contacts.Contact')),
                ('title', models.CharField(max_length=250, blank=True)),
                ('short_name', models.CharField(db_index=True, max_length=250, blank=True)),
                ('long_name', models.CharField(db_index=True, max_length=250, blank=True)),
                ('suffix', models.CharField(max_length=250, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(default='', max_length=1, blank=True, choices=[('M', 'Male'), ('F', 'Female')])),
            ],
            options={
                'ordering': ('long_name',),
                'abstract': False,
                'get_latest_by': 'created_at',
                'verbose_name_plural': 'people',
            },
            bases=('contacts.contact',),
        ),
        migrations.CreateModel(
            name='PersonOrganisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, blank=True)),
                ('department', models.CharField(max_length=250, blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('organisation', models.ForeignKey(related_name='positions', to='contacts.Organisation')),
                ('person', models.ForeignKey(related_name='occupations', to='contacts.Person')),
            ],
            options={
                'verbose_name': 'employment',
                'verbose_name_plural': 'employment',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, blank=True)),
                ('value', models.CharField(db_index=True, max_length=250, verbose_name='Number', blank=True)),
                ('type', models.CharField(blank=True, max_length=50, db_index=True, choices=[('Landline', 'Landline'), ('Mobile', 'Mobile'), ('Fax', 'Fax'), ('VOIP', 'VOIP')])),
            ],
            options={
                'ordering': ['contact_phones__order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, blank=True)),
                ('value', models.URLField(db_index=True, max_length=255, verbose_name='URL', blank=True)),
            ],
            options={
                'ordering': ['contact_websites__order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='organisations',
            field=models.ManyToManyField(related_name='people', null=True, through='contacts.PersonOrganisation', to='contacts.Organisation', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(related_name='contact', null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactwebsite',
            name='contact',
            field=models.ForeignKey(related_name='+', to='contacts.Contact'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactwebsite',
            name='website',
            field=models.ForeignKey(related_name='contact_websites', to='contacts.Website'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='contactwebsite',
            unique_together=set([('contact', 'website')]),
        ),
        migrations.AddField(
            model_name='contactphone',
            name='contact',
            field=models.ForeignKey(related_name='+', to='contacts.Contact'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactphone',
            name='phone',
            field=models.ForeignKey(related_name='contact_phones', to='contacts.Phone'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='contactphone',
            unique_together=set([('contact', 'phone')]),
        ),
        migrations.AddField(
            model_name='contactnickname',
            name='contact',
            field=models.ForeignKey(related_name='+', to='contacts.Contact'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactnickname',
            name='nickname',
            field=models.ForeignKey(related_name='contact_nicknames', to='contacts.Nickname'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='contactnickname',
            unique_together=set([('contact', 'nickname')]),
        ),
        migrations.AddField(
            model_name='contactinstantmessengerhandle',
            name='contact',
            field=models.ForeignKey(related_name='+', to='contacts.Contact'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactinstantmessengerhandle',
            name='instant_messenger_handle',
            field=models.ForeignKey(related_name='contact_instant_messenger_handles', to='contacts.InstantMessengerHandle'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='contactinstantmessengerhandle',
            unique_together=set([('contact', 'instant_messenger_handle')]),
        ),
        migrations.AddField(
            model_name='contactemail',
            name='contact',
            field=models.ForeignKey(related_name='+', to='contacts.Contact'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactemail',
            name='email',
            field=models.ForeignKey(related_name='contact_emails', to='contacts.Email'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='contactemail',
            unique_together=set([('contact', 'email')]),
        ),
        migrations.AddField(
            model_name='contactaddress',
            name='contact',
            field=models.ForeignKey(related_name='+', to='contacts.Contact'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='contactaddress',
            unique_together=set([('contact', 'address')]),
        ),
        migrations.AddField(
            model_name='contact',
            name='addresses',
            field=models.ManyToManyField(related_name='+', null=True, through='contacts.ContactAddress', to='contacts.Address', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='created_by',
            field=models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='emails',
            field=models.ManyToManyField(related_name='+', null=True, through='contacts.ContactEmail', to='contacts.Email', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='groups',
            field=models.ManyToManyField(related_name='contacts', null=True, to='contacts.ContactGroup', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='instant_messenger_handles',
            field=models.ManyToManyField(related_name='+', null=True, through='contacts.ContactInstantMessengerHandle', to='contacts.InstantMessengerHandle', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='nicknames',
            field=models.ManyToManyField(related_name='+', null=True, through='contacts.ContactNickname', to='contacts.Nickname', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='phones',
            field=models.ManyToManyField(related_name='+', null=True, through='contacts.ContactPhone', to='contacts.Phone', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='updated_by',
            field=models.ForeignKey(related_name='+', editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='websites',
            field=models.ManyToManyField(related_name='+', null=True, through='contacts.ContactWebsite', to='contacts.Website', blank=True),
            preserve_default=True,
        ),
    ]
