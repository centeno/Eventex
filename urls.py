from django.conf.urls.defaults import *
from django.conf import settings
from core.views import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', homepage, {'template': 'index.htm'}),
    (r'^inscricao/', include("subscription.urls", namespace="subscription")),
    (r'^admin/', include('django.contrib.admin.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT }
    ),
)
