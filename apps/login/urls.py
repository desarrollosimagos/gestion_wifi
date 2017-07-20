from django.conf.urls import url
from .views import base_view # Se importan las vistas

urlpatterns = [
	url(r'^$', 'apps.login.views.base_view', name="home",), # Pagina de inicio
	
]
