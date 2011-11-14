# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ArticleComment'
        db.create_table('articlesComments_articlecomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('show_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['articles.Article'])),
        ))
        db.send_create_signal('articlesComments', ['ArticleComment'])


    def backwards(self, orm):
        
        # Deleting model 'ArticleComment'
        db.delete_table('articlesComments_articlecomment')


    models = {
        'articles.article': {
            'Meta': {'ordering': "['name']", 'object_name': 'Article'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'articles'", 'symmetrical': 'False', 'to': "orm['people.Man']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'preview': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'articlesComments.articlecomment': {
            'Meta': {'ordering': "['-created']", 'object_name': 'ArticleComment'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': "orm['articles.Article']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'show_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'people.man': {
            'Meta': {'ordering': "['name']", 'object_name': 'Man'},
            'contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'link': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['articlesComments']
