from django.conf.urls import url
from .views import mostrar_totales, mostrar_dias

urlpatterns = [
    url(r'^$','apps.grafica.views.mostrar_totales'),
    url(r'^dias/','apps.grafica.views.mostrar_dias'),
]
