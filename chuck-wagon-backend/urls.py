from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import trucks.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chuck-wagon-backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', trucks.views.index, name='index'),
    url(r'^trucks/near/(.*)/(.*)/$', trucks.views.nearby_trucks, name='nearby_trucks'),
    url(r'^trucks/within/(.*)/of/(.*)/(.*)/$', trucks.views.trucks_within_distance, name='trucks_within_distance'),
    url(r'^trucks$', trucks.views.trucks, name='trucks'),
    url(r'^admin/', include(admin.site.urls)),

)
