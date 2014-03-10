# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'line_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'line', ['City'])

        # Adding model 'Viewspot'
        db.create_table(u'line_viewspot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['line.City'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'line', ['Viewspot'])

        # Adding model 'Hotel'
        db.create_table(u'line_hotel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['line.City'])),
        ))
        db.send_create_signal(u'line', ['Hotel'])

        # Adding model 'Restau'
        db.create_table(u'line_restau', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['line.City'])),
        ))
        db.send_create_signal(u'line', ['Restau'])

        # Adding model 'Linepoint'
        db.create_table(u'line_linepoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['line.Viewspot'])),
        ))
        db.send_create_signal(u'line', ['Linepoint'])

        # Adding model 'Line'
        db.create_table(u'line_line', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'line', ['Line'])

        # Adding M2M table for field points on 'Line'
        m2m_table_name = db.shorten_name(u'line_line_points')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('line', models.ForeignKey(orm[u'line.line'], null=False)),
            ('linepoint', models.ForeignKey(orm[u'line.linepoint'], null=False))
        ))
        db.create_unique(m2m_table_name, ['line_id', 'linepoint_id'])

        # Adding model 'Comment'
        db.create_table(u'line_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['visitor.Visitor'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('viewspot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['line.Viewspot'])),
            ('hotel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['line.Hotel'])),
            ('restau', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['line.Restau'])),
        ))
        db.send_create_signal(u'line', ['Comment'])

        # Adding model 'Img'
        db.create_table(u'line_img', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('hotel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['line.Hotel'])),
            ('restau', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['line.Restau'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['line.City'])),
        ))
        db.send_create_signal(u'line', ['Img'])

        # Adding model 'Status'
        db.create_table(u'line_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['visitor.Visitor'])),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'line', ['Status'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table(u'line_city')

        # Deleting model 'Viewspot'
        db.delete_table(u'line_viewspot')

        # Deleting model 'Hotel'
        db.delete_table(u'line_hotel')

        # Deleting model 'Restau'
        db.delete_table(u'line_restau')

        # Deleting model 'Linepoint'
        db.delete_table(u'line_linepoint')

        # Deleting model 'Line'
        db.delete_table(u'line_line')

        # Removing M2M table for field points on 'Line'
        db.delete_table(db.shorten_name(u'line_line_points'))

        # Deleting model 'Comment'
        db.delete_table(u'line_comment')

        # Deleting model 'Img'
        db.delete_table(u'line_img')

        # Deleting model 'Status'
        db.delete_table(u'line_status')


    models = {
        u'line.city': {
            'Meta': {'object_name': 'City'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'line.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['visitor.Visitor']"}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['line.Hotel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'restau': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['line.Restau']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'viewspot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['line.Viewspot']"})
        },
        u'line.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['line.City']"}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'line.img': {
            'Meta': {'object_name': 'Img'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['line.City']"}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['line.Hotel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restau': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['line.Restau']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'line.line': {
            'Meta': {'object_name': 'Line'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'points': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['line.Linepoint']", 'symmetrical': 'False'})
        },
        u'line.linepoint': {
            'Meta': {'object_name': 'Linepoint'},
            'day': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['line.Viewspot']"})
        },
        u'line.restau': {
            'Meta': {'object_name': 'Restau'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['line.City']"}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'line.status': {
            'Meta': {'object_name': 'Status'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['visitor.Visitor']"}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'line.viewspot': {
            'Meta': {'object_name': 'Viewspot'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['line.City']"}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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

    complete_apps = ['line']