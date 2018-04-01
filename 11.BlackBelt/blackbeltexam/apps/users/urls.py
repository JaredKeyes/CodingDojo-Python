from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^new$', views.new),
    url(r'^create$',views.create, name='create'),
    url(r'^success$',views.success, name='success'),
    url(r'^authenticate$',views.authenticate, name='authenticate'),
    url(r'^logout$',views.logout, name='logout'),
    url(r'^home$', views.home, name='home'),
    url(r'^add$', views.add, name='add'),
    url(r'^add_travel$', views.add_travel, name='add_travel'),
    url(r'^join/(?P<id>\d+)$', views.join, name='join'),
    url(r'^trip_detail/(?P<id>\d+)$', views.trip_detail, name='trip_detail')
]