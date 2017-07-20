from django.conf.urls import patterns, include, url
from django.contrib import admin

import settings

# router = DefaultRouter()
# router.register(r'registro', FichaPersonalViewSet)
urlpatterns = patterns('',
                       url(r'^', include('apps.urls')),
                      
                       )
