from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^event/new/$', views.event_new, name='event_new'),
	url(r'^event/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),
]