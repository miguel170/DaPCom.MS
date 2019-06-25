from django.conf.urls import url
from . import views

urlpatterns = [
    
    # /pdi/
    url(r'^$', views.index, name = 'Personal Data Inventory'),
    
    # /pdi/activity#/
    url(r'^(?P<activity_id>[0-9]+)/$', views.update, name = 'Update PDI'),
]