from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^getstate$', 'Switch.views.getstate', name='getstate'),
    url(r'^setstate$', 'Switch.views.setstate', name='setstate'),
)
