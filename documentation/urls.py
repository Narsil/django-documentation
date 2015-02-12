from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('documentation.views',
    url(r'^(?P<path>.*)$', 'documentation', name="documentation"),
)
