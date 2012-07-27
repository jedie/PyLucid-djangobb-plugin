# coding: utf-8

from django.conf.urls import patterns, include
from django.contrib import admin

#from sitemap import SitemapForum, SitemapTopic

admin.autodiscover()

#sitemaps = {
#    'forum': SitemapForum,
#    'topic': SitemapTopic,
#}

urlpatterns = patterns('',
    # Sitemap
#    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Apps
    (r'^account/', include('django_authopenid.urls')),
    (r'^pm/', include('django_messages.urls')),
    (r'^', include('djangobb_forum.urls', namespace='djangobb')),
)
