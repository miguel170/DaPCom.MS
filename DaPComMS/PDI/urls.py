from django.conf.urls import url
from . import views

app_name = 'PDI'

urlpatterns = [
    
    # /pdi/
    url(r'^$', views.index, name = 'main'),
    
    # /pdi/activity#/
    url(r'^(?P<activity_id>[0-9]+)/$', views.update, name = 'update'),
]