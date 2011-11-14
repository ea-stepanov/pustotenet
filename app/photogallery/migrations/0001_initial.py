# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PhotoAlbum'
        db.create_table('photogallery_photoalbum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('last_update_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('link', self.gf('django.db.models.fields.SlugField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal('photogallery', ['PhotoAlbum'])

        # Adding model 'Photo'
        db.create_table('photogallery_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photos', to=orm['photogallery.PhotoAlbum'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('photogallery', ['Photo'])


    def backwards(self, orm):
        
        # Deleting model 'PhotoAlbum'
        db.delete_table('photogallery_photoalbum')

        # Deleting model 'Photo'
        db.delete_table('photogallery_photo')


    models = {
        'photogallery.photo': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': "orm['photogallery.PhotoAlbum']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'photogallery.photoalbum': {
            'Meta': {'ordering': "['name']", 'object_name': 'PhotoAlbum'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update_at': ('django.db.models.fields.DateTimeField', [], {}),
            'link': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['photogallery']
