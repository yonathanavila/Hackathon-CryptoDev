from django.shortcuts import render
from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy


# Create your views here.
class clsTemplateviewHome(TemplateView):
  template_name = "core/home.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = "Menu Principal"

    return context
