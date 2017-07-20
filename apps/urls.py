from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^', include('apps.login.urls')),  # Url direccion a la URL login
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^cantidad/', include('apps.grafica.urls')),
                       url(r'^grafica/', include('apps.grafica.urls')),
)

