# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Visitor'
        db.create_table(u'visitor_visitor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('regdate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('headimg', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'visitor', ['Visitor'])


    def backwards(self, orm):
        # Deleting model 'Visitor'
        db.delete_table(u'visitor_visitor')


    models = {
        u'visitor.visitor': {
            'Meta': {'object_name': 'Visitor'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'headimg': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'regdate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['visitor']