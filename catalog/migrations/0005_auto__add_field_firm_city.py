# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Firm.city'
        db.add_column(u'catalog_firm', 'city',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['catalog.City']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Firm.city'
        db.delete_column(u'catalog_firm', 'city_id')


    models = {
        u'catalog.category': {
            'Meta': {'object_name': 'Category'},
            'alt_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['catalog.Category']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'catalog.city': {
            'Meta': {'object_name': 'City'},
            'alt_name': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'catalog.firm': {
            'Meta': {'object_name': 'Firm'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'alt_title': ('django.db.models.fields.SlugField', [], {'max_length': '250'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalog.Category']", 'symmetrical': 'False'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['catalog']