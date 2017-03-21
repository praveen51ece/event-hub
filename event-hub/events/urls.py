from django.conf.urls import patterns, include, url
from django.contrib import admin
import sys
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

sys.setrecursionlimit(10000)

urlpatterns = patterns('',
	url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    # Examples:
    # url(r'^$', 'events.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('event.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT, 'show_indexes': False}),

)
urlpatterns += staticfiles_urlpatterns()
