from django.urls import path
from .views import *

urlpatterns = [
  path('', clsHome.as_view(), name='home'),
  path('subir/firma/', clsSubirFirmas.as_view(), name='subir'),
  path('firmar/', clsTemplateviewHome.as_view(), name='menu'),
  path('list/', clsListFirmas.as_view(), name="listado-firmas"),
]
