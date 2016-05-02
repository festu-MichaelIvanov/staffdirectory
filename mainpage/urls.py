from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^authpage/', include('authpage.urls')),
	url(r'^searchingpage/', include('searchingpage.urls')),
]
