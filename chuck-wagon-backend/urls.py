from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import trucks.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chuck-wagon-backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', trucks.views.index, name='index'),
    url(r'^db', trucks.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)
