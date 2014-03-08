# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Knight'
        db.delete_table(u'onroad_knight')

        # Adding model 'Img'
        db.create_table(u'onroad_img', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('hotel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.Hotel'])),
            ('restau', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.Restau'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.City'])),
        ))
        db.send_create_signal(u'onroad', ['Img'])

        # Adding model 'Status'
        db.create_table(u'onroad_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['visitor.Visitor'])),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'onroad', ['Status'])

        # Adding model 'Viewspot'
        db.create_table(u'onroad_viewspot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.City'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'onroad', ['Viewspot'])

        # Adding model 'Hotel'
        db.create_table(u'onroad_hotel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.City'])),
            ('viewspot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.Viewspot'])),
        ))
        db.send_create_signal(u'onroad', ['Hotel'])

        # Adding model 'Comment'
        db.create_table(u'onroad_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['visitor.Visitor'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('viewspot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.Viewspot'])),
            ('hotel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.Hotel'])),
            ('restau', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.Restau'])),
        ))
        db.send_create_signal(u'onroad', ['Comment'])

        # Adding model 'Restau'
        db.create_table(u'onroad_restau', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.City'])),
            ('viewspot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.Viewspot'])),
        ))
        db.send_create_signal(u'onroad', ['Restau'])

        # Adding model 'Linepoint'
        db.create_table(u'onroad_linepoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('viewspot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.Viewspot'])),
            ('hotel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.Hotel'])),
            ('restau', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.Restau'])),
            ('line', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onroad.Line'])),
        ))
        db.send_create_signal(u'onroad', ['Linepoint'])

        # Adding model 'Line'
        db.create_table(u'onroad_line', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['visitor.Visitor'])),
        ))
        db.send_create_signal(u'onroad', ['Line'])

        # Adding model 'City'
        db.create_table(u'onroad_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'onroad', ['City'])


    def backwards(self, orm):
        # Adding model 'Knight'
        db.create_table(u'onroad_knight', (
            ('of_the_round_table', self.gf('django.db.models.fields.BooleanField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'onroad', ['Knight'])

        # Deleting model 'Img'
        db.delete_table(u'onroad_img')

        # Deleting model 'Status'
        db.delete_table(u'onroad_status')

        # Deleting model 'Viewspot'
        db.delete_table(u'onroad_viewspot')

        # Deleting model 'Hotel'
        db.delete_table(u'onroad_hotel')

        # Deleting model 'Comment'
        db.delete_table(u'onroad_comment')

        # Deleting model 'Restau'
        db.delete_table(u'onroad_restau')

        # Deleting model 'Linepoint'
        db.delete_table(u'onroad_linepoint')

        # Deleting model 'Line'
        db.delete_table(u'onroad_line')

        # Deleting model 'City'
        db.delete_table(u'onroad_city')


    models = {
        u'onroad.city': {
            'Meta': {'object_name': 'City'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'onroad.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['visitor.Visitor']"}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.Hotel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'restau': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.Restau']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'viewspot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.Viewspot']"})
        },
        u'onroad.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.City']"}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'viewspot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.Viewspot']"})
        },
        u'onroad.img': {
            'Meta': {'object_name': 'Img'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.City']"}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.Hotel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restau': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.Restau']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'onroad.line': {
            'Meta': {'object_name': 'Line'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['visitor.Visitor']"}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'onroad.linepoint': {
            'Meta': {'object_name': 'Linepoint'},
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.Hotel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.Line']"}),
            'restau': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.Restau']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'viewspot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.Viewspot']"})
        },
        u'onroad.restau': {
            'Meta': {'object_name': 'Restau'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.City']"}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'viewspot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.Viewspot']"})
        },
        u'onroad.status': {
            'Meta': {'object_name': 'Status'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['visitor.Visitor']"}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'onroad.viewspot': {
            'Meta': {'object_name': 'Viewspot'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onroad.City']"}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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

    complete_apps = ['onroad']