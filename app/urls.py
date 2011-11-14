from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.main', name='main'),
    url(r'^photogallery/$', 'photogallery.views.photogallery', name='photogallery'),
    url(r'^(photogallery/[A-Za-z\-]+)/$', 'photogallery.views.view_gallery', name='photoalbum'),
    url(r'^people/$', 'people.views.get_people_list', name='people'),
    url(r'^(people/[A-Za-z\-]+)/$', 'people.views.get_man', name='man'),
    url(r'^articles/$', 'articles.views.get_articles_list', name='articles'),
    url(r'^(articles/[A-Za-z\-]+)/$', 'articles.views.view_article', name='article'),
    url(r'^videos/$', 'videos.views.get_videos_list', name='videos'),
    url(r'^(videos/[A-Za-z\-]+)/$', 'videos.views.view_video'),
    url(r'^people/[A-Za-z\-]+/materials-(?P<id>\d+)', 'people.views.get_man_materials'),
    # url(r'^pustotenet/', include('pustotenet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^photogallery/', 'pustotenet.')
)
