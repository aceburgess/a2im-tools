from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^event/([0-9]+)/$', views.event, name='event'),
]