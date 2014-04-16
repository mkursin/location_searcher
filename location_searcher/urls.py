from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from searcher import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_location_by_ip/', views.get_location_by_ip, name='get_location_by_ip'),
)
