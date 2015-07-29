from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.contrib import admin

import autocomplete_light

autocomplete_light.autodiscover()

urlpatterns = [
	url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^', include(admin.site.urls)),
    url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^staff/', include('staff.urls', namespace='staff')),
]
