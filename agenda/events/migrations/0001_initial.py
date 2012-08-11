# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table('events_region', (
            ('id', self.gf('django.db.models.fields.PositiveSmallIntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('events', ['Region'])

        # Adding model 'City'
        db.create_table('events_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Region'])),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('events', ['City'])

        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('tags', self.gf('agenda.tagging.fields.TagField')(max_length=255, blank=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('scope', self.gf('django.db.models.fields.CharField')(default='L', max_length=1)),
            ('submission_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('venue', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.City'])),
            ('latitude', self.gf('django.db.models.fields.FloatField')(default=0, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(default=0, blank=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('moderator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='moderated_events', null=True, to=orm['auth.User'])),
            ('moderated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('decision_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('submiter_email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
        ))
        db.send_create_signal('events', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table('events_region')

        # Deleting model 'City'
        db.delete_table('events_city')

        # Deleting model 'Event'
        db.delete_table('events_event')


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'events.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Region']"})
        },
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.City']"}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'decision_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'moderated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'moderator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'moderated_events'", 'null': 'True', 'to': "orm['auth.User']"}),
            'scope': ('django.db.models.fields.CharField', [], {'default': "'L'", 'max_length': '1'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'submission_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'submiter_email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'tags': ('agenda.tagging.fields.TagField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'events.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.PositiveSmallIntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['events']