# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='addresses',
            field=models.ManyToManyField(related_name='+', through='contacts.ContactAddress', to='contacts.Address', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='emails',
            field=models.ManyToManyField(related_name='+', through='contacts.ContactEmail', to='contacts.Email', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='groups',
            field=models.ManyToManyField(related_name='contacts', to='contacts.ContactGroup', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='instant_messenger_handles',
            field=models.ManyToManyField(related_name='+', through='contacts.ContactInstantMessengerHandle', to='contacts.InstantMessengerHandle', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='nicknames',
            field=models.ManyToManyField(related_name='+', through='contacts.ContactNickname', to='contacts.Nickname', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phones',
            field=models.ManyToManyField(related_name='+', through='contacts.ContactPhone', to='contacts.Phone', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='websites',
            field=models.ManyToManyField(related_name='+', through='contacts.ContactWebsite', to='contacts.Website', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='organisations',
            field=models.ManyToManyField(related_name='people', through='contacts.PersonOrganisation', to='contacts.Organisation', blank=True),
        ),
    ]
