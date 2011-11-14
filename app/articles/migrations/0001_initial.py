# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Article'
        db.create_table('articles_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('preview', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('link', self.gf('django.db.models.fields.SlugField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal('articles', ['Article'])

        # Adding M2M table for field authors on 'Article'
        db.create_table('articles_article_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm['articles.article'], null=False)),
            ('man', models.ForeignKey(orm['people.man'], null=False))
        ))
        db.create_unique('articles_article_authors', ['article_id', 'man_id'])


    def backwards(self, orm):
        
        # Deleting model 'Article'
        db.delete_table('articles_article')

        # Removing M2M table for field authors on 'Article'
        db.delete_table('articles_article_authors')


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

    complete_apps = ['articles']
