# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table('twitter_account', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('consumer_key', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('consumer_secret', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('access_token_secret', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('twitter', ['Account'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table('twitter_account')


    models = {
        'twitter.account': {
            'Meta': {'object_name': 'Account'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'access_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'consumer_secret': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['twitter']