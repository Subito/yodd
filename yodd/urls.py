from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^update/', 'updater.views.update', name='update'),
    url(r'^admin/', include(admin.site.urls)),
)
