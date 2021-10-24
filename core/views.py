from django.shortcuts import render
from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy


# Create your views here.
class clsTemplateviewHome(CreateView):
  template_name = "core/firmar/firmar.html"
  form_class = frmUserWallet
  success_url = reverse_lazy('menu')


class clsHome(TemplateView):
  template_name = "core/home.html"
  model = UserWallet

  def post(self, request, *args, **kwargs):
    print("Holaa")
    PoapLink_qs = PoapLink.objects.last()
    for i in PoapLink_qs:
      print(i)
    # texto = open()
    return


class clsSubirFirmas(CreateView):
  template_name = "core/subir_links/subir_firmas.html"
  form_class = frmFile
  success_url = reverse_lazy('subir')


class clsListFirmas(ListView):
  template_name = "core/list_firmas/list_firmas.html"
  model = UserWallet
