from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.searchingpage),
    url(r'^search', views.search),
]