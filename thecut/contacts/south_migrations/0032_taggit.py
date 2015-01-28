# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from thecut.authorship.settings import AUTH_USER_MODEL
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

try:
    from django.utils.text import slugify
except ImportError:
    # Pre-Django 1.5
    from django.template.defaultfilters import slugify


# From django-tagging ---------------------------------------------------------

from django.utils.encoding import force_unicode

def parse_tag_input(input):
    """
    Parses tag input, with multiple word input being activated and
    delineated by commas and double quotes. Quotes take precedence, so
    they may contain commas.

    Returns a sorted list of unique tag names.
    """
    if not input:
        return []

    input = force_unicode(input)

    # Special case - if there are no commas or double quotes in the
    # input, we don't *do* a recall... I mean, we know we only need to
    # split on spaces.
    if u',' not in input and u'"' not in input:
        words = list(set(split_strip(input, u' ')))
        words.sort()
        return words

    words = []
    buffer = []
    # Defer splitting of non-quoted sections until we know if there are
    # any unquoted commas.
    to_be_split = []
    saw_loose_comma = False
    open_quote = False
    i = iter(input)
    try:
        while 1:
            c = i.next()
            if c == u'"':
                if buffer:
                    to_be_split.append(u''.join(buffer))
                    buffer = []
                # Find the matching quote
                open_quote = True
                c = i.next()
                while c != u'"':
                    buffer.append(c)
                    c = i.next()
                if buffer:
                    word = u''.join(buffer).strip()
                    if word:
                        words.append(word)
                    buffer = []
                open_quote = False
            else:
                if not saw_loose_comma and c == u',':
                    saw_loose_comma = True
                buffer.append(c)
    except StopIteration:
        # If we were parsing an open quote which was never closed treat
        # the buffer as unquoted.
        if buffer:
            if open_quote and u',' in buffer:
                saw_loose_comma = True
            to_be_split.append(u''.join(buffer))
    if to_be_split:
        if saw_loose_comma:
            delimiter = u','
        else:
            delimiter = u' '
        for chunk in to_be_split:
            words.extend(split_strip(chunk, delimiter))
    words = list(set(words))
    words.sort()
    return words

def split_strip(input, delimiter=u','):
    """
    Splits ``input`` on ``delimiter``, stripping each resulting string
    and returning a list of non-empty strings.
    """
    if not input:
        return []

    words = [w.strip() for w in input.split(delimiter)]
    return [w for w in words if w]

# End code from django-tagging ------------------------------------------------

def generate_unique_slug(text, queryset, slug_field='slug', iteration=0):
    """Generate a unique slug for a model from the provided text."""
    slug = slugify(text)
    if iteration > 0:
        slug = '{0}-{1}'.format(iteration, slug)
    slug = slug[:50]

    try:
        queryset.get(**{slug_field: slug})
    except ObjectDoesNotExist:
        return slug
    else:
        iteration += 1
        return generate_unique_slug(text, queryset=queryset,
                                    slug_field=slug_field, iteration=iteration)


class TagDuplicator(object):

    def __init__(self, orm):
        self.orm = orm

    def duplicate_tags(self, obj):
        # Get the names of the obj's `django-tagging` tags.
        tag_names = parse_tag_input(obj.tags)

        # For each django-tagging tag which doesn't already have django-taggit
        # equivalent, create one.
        for name in tag_names:
            tag = self.get_or_create_taggit_tag(name)
            self.create_taggit_tagged_item(tag, obj)

    def get_or_create_taggit_tag(self, name):
        try:
            # Get a taggit-tag with the given name.
            tag = self.orm['taggit.Tag'].objects.get(name=name)
        except self.orm['taggit.Tag'].DoesNotExist:
            # If one doesn't already exist, create it, ensuring we don't
            # conflict with the slugs of any exisiting taggit-tags.
            queryset = self.orm['taggit.Tag'].objects.all()
            slug = generate_unique_slug(name, queryset)
            tag = self.orm['taggit.Tag'].objects.create(name=name, slug=slug)

        return tag

    def create_taggit_tagged_item(self, tag, obj):
        obj_content_type = ContentType.objects.get_for_model(obj)
        item = self.orm['taggit.TaggedItem'].objects.create(
            tag=tag, content_type_id=obj_content_type.pk, object_id=obj.pk)


class Migration(DataMigration):

    depends_on = (
        ('taggit', '0002_unique_tagnames'),
    )

    def forwards(self, orm):
        duplicator = TagDuplicator(orm)

        for obj in orm.Contact.objects.all():
            duplicator.duplicate_tags(obj)

        for obj in orm.ContactGroup.objects.all():
            duplicator.duplicate_tags(obj)

    def backwards(self, orm):
        pass

    models = {
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
        AUTH_USER_MODEL: {
            'Meta': {'object_name': AUTH_USER_MODEL.split('.')[-1]},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
        },
        u'contacts.address': {
            'Meta': {'ordering': "[u'contact_addresses__order']", 'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'default': "u'AU'", 'max_length': '2', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'blank': 'True'}),
            'street': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'contacts.contact': {
            'Meta': {'ordering': "(u'-created_at',)", 'object_name': 'Contact'},
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': u"orm['contacts.Address']", 'through': u"orm['contacts.ContactAddress']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
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
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            'websites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'+'", 'to': u"orm['contacts.Website']", 'through': u"orm['contacts.ContactWebsite']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'})
        },
        u'contacts.contactaddress': {
            'Meta': {'ordering': "(u'order',)", 'unique_together': "((u'contact', u'address'),)", 'object_name': 'ContactAddress'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_addresses'", 'to': u"orm['contacts.Address']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'contacts.contactemail': {
            'Meta': {'ordering': "(u'order',)", 'unique_together': "((u'contact', u'email'),)", 'object_name': 'ContactEmail'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['contacts.Contact']"}),
            'email': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_emails'", 'to': u"orm['contacts.Email']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'contacts.contactgroup': {
            'Meta': {'ordering': "(u'name', u'-created_at')", 'object_name': 'ContactGroup'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['{0}']".format(AUTH_USER_MODEL)})
        },
        u'contacts.contactinstantmessengerhandle': {
            'Meta': {'ordering': "(u'order',)", 'unique_together': "((u'contact', u'instant_messenger_handle'),)", 'object_name': 'ContactInstantMessengerHandle'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instant_messenger_handle': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_instant_messenger_handles'", 'to': u"orm['contacts.InstantMessengerHandle']"}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'contacts.contactnickname': {
            'Meta': {'ordering': "(u'order',)", 'unique_together': "((u'contact', u'nickname'),)", 'object_name': 'ContactNickname'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_nicknames'", 'to': u"orm['contacts.Nickname']"}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'contacts.contactphone': {
            'Meta': {'ordering': "(u'order',)", 'unique_together': "((u'contact', u'phone'),)", 'object_name': 'ContactPhone'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'phone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_phones'", 'to': u"orm['contacts.Phone']"})
        },
        u'contacts.contactwebsite': {
            'Meta': {'ordering': "(u'order',)", 'unique_together': "((u'contact', u'website'),)", 'object_name': 'ContactWebsite'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contact_websites'", 'to': u"orm['contacts.Website']"})
        },
        u'contacts.email': {
            'Meta': {'ordering': "[u'contact_emails__order']", 'object_name': 'Email'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'value': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '254', 'blank': 'True'})
        },
        u'contacts.instantmessengerhandle': {
            'Meta': {'ordering': "[u'contact_instant_messenger_handles__order']", 'object_name': 'InstantMessengerHandle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '254', 'blank': 'True'})
        },
        u'contacts.nickname': {
            'Meta': {'ordering': "[u'contact_nicknames__order']", 'object_name': 'Nickname'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'blank': 'True'})
        },
        u'contacts.organisation': {
            'Meta': {'ordering': "(u'name',)", 'object_name': 'Organisation'},
            'abn': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '11', 'blank': 'True'}),
            u'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'blank': 'True'})
        },
        u'contacts.person': {
            'Meta': {'ordering': "(u'long_name',)", 'object_name': 'Person'},
            u'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '1', 'blank': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'blank': 'True'}),
            'organisations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'people'", 'to': u"orm['contacts.Organisation']", 'through': u"orm['contacts.PersonOrganisation']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "u'contact'", 'unique': 'True', 'null': 'True', 'to': u"orm['{0}']".format(AUTH_USER_MODEL)})
        },
        u'contacts.personorganisation': {
            'Meta': {'object_name': 'PersonOrganisation'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'positions'", 'to': u"orm['contacts.Organisation']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'occupations'", 'to': u"orm['contacts.Person']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        u'contacts.phone': {
            'Meta': {'ordering': "[u'contact_phones__order']", 'object_name': 'Phone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '250', 'blank': 'True'})
        },
        u'contacts.website': {
            'Meta': {'ordering': "[u'contact_websites__order']", 'object_name': 'Website'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'value': ('django.db.models.fields.URLField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contacts']
    symmetrical = True
