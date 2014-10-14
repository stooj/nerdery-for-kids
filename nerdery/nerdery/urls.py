from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nerdery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'nerdery_servers.views.home_page', name='home'),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'', include('django_browserid.urls')),
)
