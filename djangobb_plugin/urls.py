# coding: utf-8

from django.conf.urls import patterns, include
from django.contrib import admin

#from sitemap import SitemapForum, SitemapTopic

admin.autodiscover()

try:
    import djangobb_code_comments
except ImportError:
    djangobb_code_comments = False
else:
    djangobb_code_comments = True

urlpatterns = patterns('',
    # Sitemap
#    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Apps
    (r'^account/', include('django_authopenid.urls')),
    (r'^pm/', include('django_messages.urls')),
    (r'^', include('djangobb_forum.urls', namespace='djangobb')),
)
if djangobb_code_comments:
    urlpatterns += patterns('',
        (r'^', include('djangobb_code_comments.urls')),
    )
