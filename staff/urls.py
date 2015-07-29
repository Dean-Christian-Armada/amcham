from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
				# url(r'^$', views.index, name='index'),
				# auto-complete-light url requirement
				url(r'^navigation_autocomplete/$', views.navigation_autocomplete, name='navigation_autocomplete'),
				)