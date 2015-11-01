# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductPhoto'
        db.create_table(u'catalog_productphoto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('main', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Product'])),
        ))
        db.send_create_signal(u'catalog', ['ProductPhoto'])

        # Adding model 'Product'
        db.create_table(u'catalog_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('alt_title', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=4)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('firm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Firm'])),
            ('seo_title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('seo_keywords', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('seo_description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'catalog', ['Product'])


    def backwards(self, orm):
        # Deleting model 'ProductPhoto'
        db.delete_table(u'catalog_productphoto')

        # Deleting model 'Product'
        db.delete_table(u'catalog_product')


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
            'seo_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'seo_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
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
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'category'", 'symmetrical': 'False', 'to': u"orm['catalog.Category']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'seo_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'seo_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'catalog.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alt_title': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Firm']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '4'}),
            'seo_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'seo_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'catalog.productphoto': {
            'Meta': {'object_name': 'ProductPhoto'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Product']"})
        }
    }

    complete_apps = ['catalog']