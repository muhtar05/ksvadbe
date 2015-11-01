# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'catalog_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('alt_name', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['catalog.Category'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'catalog', ['Category'])

        # Adding model 'Firm'
        db.create_table(u'catalog_firm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('alt_title', self.gf('django.db.models.fields.SlugField')(max_length=250)),
            ('info', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'catalog', ['Firm'])

        # Adding M2M table for field category on 'Firm'
        m2m_table_name = db.shorten_name(u'catalog_firm_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('firm', models.ForeignKey(orm[u'catalog.firm'], null=False)),
            ('category', models.ForeignKey(orm[u'catalog.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['firm_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'catalog_category')

        # Deleting model 'Firm'
        db.delete_table(u'catalog_firm')

        # Removing M2M table for field category on 'Firm'
        db.delete_table(db.shorten_name(u'catalog_firm_category'))


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
        u'catalog.firm': {
            'Meta': {'object_name': 'Firm'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'alt_title': ('django.db.models.fields.SlugField', [], {'max_length': '250'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalog.Category']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['catalog']