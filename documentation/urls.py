from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'documentation.views',

    url(r'^$', 'documentation', 'index.html'),
    url(r'^(?P<path>.*)$', 'documentation', name="path"),
)
