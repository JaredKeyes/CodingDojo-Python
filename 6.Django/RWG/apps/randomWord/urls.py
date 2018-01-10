from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^generate$', views.generate),
    url(r'^refresh$', views.refresh),
    url(r'^$', views.index),
    url(r'^randomWord$', views.index)
    
]