from django.urls import path
from .views import *

urlpatterns = [
  path('', clsTemplateviewHome.as_view(), name='menu'),
]
