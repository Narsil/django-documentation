from django.conf.urls import patterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('documentation.views',
    (r'^(?P<path>.*)$', 'documentation'),
)
