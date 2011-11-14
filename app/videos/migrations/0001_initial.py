# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Video'
        db.create_table('videos_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('inlineCode', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('link', self.gf('django.db.models.fields.SlugField')(max_length=200, db_index=True)),
        ))
        db.send_create_signal('videos', ['Video'])

        # Adding M2M table for field authors on 'Video'
        db.create_table('videos_video_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['videos.video'], null=False)),
            ('man', models.ForeignKey(orm['people.man'], null=False))
        ))
        db.create_unique('videos_video_authors', ['video_id', 'man_id'])


    def backwards(self, orm):
        
        # Deleting model 'Video'
        db.delete_table('videos_video')

        # Removing M2M table for field authors on 'Video'
        db.delete_table('videos_video_authors')


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
        'videos.video': {
            'Meta': {'object_name': 'Video'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'videos'", 'symmetrical': 'False', 'to': "orm['people.Man']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inlineCode': ('django.db.models.fields.TextField', [], {}),
            'link': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['videos']
