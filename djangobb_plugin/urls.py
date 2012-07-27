from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

from sitemap import SitemapForum, SitemapTopic
from forms import RegistrationFormUtfUsername
from djangobb_forum import settings as forum_settings
from django.views.generic.simple import direct_to_template


admin.autodiscover()

sitemaps = {
    'forum': SitemapForum,
    'topic': SitemapTopic,
}

urlpatterns = patterns('',
    # Sitemap
#    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Apps
    (r'^account/', include('django_authopenid.urls')),
    (r'^', include('djangobb_forum.urls', namespace='djangobb')),
)

# PM Extension
if (forum_settings.PM_SUPPORT):
    urlpatterns += patterns('',
        (r'^pm/', include('django_messages.urls')),
   )
