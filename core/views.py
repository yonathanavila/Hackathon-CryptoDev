from django.shortcuts import render
from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy


# Create your views here.
class clsTemplateviewHome(CreateView):
  template_name = "core/firmar/firmar.html"
  form_class = frmUserWallet
  success_url = reverse_lazy('menu')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = "Menu Principal"

    return context


class clsHome(TemplateView):
  template_name = "core/home.html"
  model = UserWallet

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = "Menu Principal"

    return context


class clsSubirFirmas(CreateView):
  template_name = "core/subir_links/subir_firmas.html"
  form_class = frmFile

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = "Menu Principal"

    return context


class clsListFirmas(ListView):
  template_name = "core/list_firmas/list_firmas.html"
  model = UserWallet

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = "Menu Principal"

    return context
