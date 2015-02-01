# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.banner'
        db.delete_column(u'events_event', 'banner')

        # Deleting field 'Event.spotlight'
        db.delete_column(u'events_event', 'spotlight')


        # Changing field 'Event.city'
        db.alter_column(u'events_event', 'city_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.City'], null=True))

        # Changing field 'Event.description'
        db.alter_column(u'events_event', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Event.url'
        db.alter_column(u'events_event', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Event.venue'
        db.alter_column(u'events_event', 'venue', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Event.longitude'
        db.alter_column(u'events_event', 'longitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Event.end_time'
        db.alter_column(u'events_event', 'end_time', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Event.latitude'
        db.alter_column(u'events_event', 'latitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Event.address'
        db.alter_column(u'events_event', 'address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):
        # Adding field 'Event.banner'
        db.add_column(u'events_event', 'banner',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Event.spotlight'
        db.add_column(u'events_event', 'spotlight',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Event.city'
        db.alter_column(u'events_event', 'city_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['events.City']))

        # Changing field 'Event.description'
        db.alter_column(u'events_event', 'description', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Event.url'
        db.alter_column(u'events_event', 'url', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'Event.venue'
        db.alter_column(u'events_event', 'venue', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'Event.longitude'
        db.alter_column(u'events_event', 'longitude', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Event.end_time'
        db.alter_column(u'events_event', 'end_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 2, 1, 0, 0)))

        # Changing field 'Event.latitude'
        db.alter_column(u'events_event', 'latitude', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Event.address'
        db.alter_column(u'events_event', 'address', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Region']"})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'announced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.City']", 'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'moderated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'moderator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'moderated_events'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'submission_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'submiter_email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'tags': ('agenda.tagging.fields.TagField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'twitter': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'events.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.PositiveSmallIntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['events']