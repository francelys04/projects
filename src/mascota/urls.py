from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from views import *


urlpatterns = patterns('',
   
    url(r'^', mascota_list_init)
      
)
