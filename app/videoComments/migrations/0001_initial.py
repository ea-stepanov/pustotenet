# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'VideoComment'
        db.create_table('videoComments_videocomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('show_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['videos.Video'])),
        ))
        db.send_create_signal('videoComments', ['VideoComment'])


    def backwards(self, orm):
        
        # Deleting model 'VideoComment'
        db.delete_table('videoComments_videocomment')


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
        'videoComments.videocomment': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'VideoComment'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'show_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': "orm['videos.Video']"})
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

    complete_apps = ['videoComments']
