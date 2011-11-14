# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Witnessing'
        db.create_table('witnessings_witnessing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.OneToOneField')(related_name='witnessing', unique=True, to=orm['people.Man'])),
            ('preview', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('link', self.gf('django.db.models.fields.SlugField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal('witnessings', ['Witnessing'])


    def backwards(self, orm):
        
        # Deleting model 'Witnessing'
        db.delete_table('witnessings_witnessing')


    models = {
        'people.man': {
            'Meta': {'ordering': "['name']", 'object_name': 'Man'},
            'contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'link': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        },
        'witnessings.witnessing': {
            'Meta': {'ordering': "['name']", 'object_name': 'Witnessing'},
            'author': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'witnessing'", 'unique': 'True', 'to': "orm['people.Man']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'preview': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['witnessings']
