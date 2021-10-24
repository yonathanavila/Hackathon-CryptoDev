from django.shortcuts import render
from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy
from urllib.request import urlopen
from django.http.response import JsonResponse
import random


# Create your views here.
class clsTemplateviewHome(CreateView):
  template_name = "core/firmar/firmar.html"
  form_class = frmUserWallet
  success_url = reverse_lazy('menu')


class clsHome(TemplateView):
  template_name = "core/home.html"
  model = UserWallet

  @staticmethod
  def post(request, *args, **kwargs):
    link = PoapLink.objects.all()
    lines = ""
    randomlink = ""
    for i in link:
      link = str(i)
    localhost = "http://localhost:8000/media/"
    url = localhost + str(link)

    try:
      openfile = urlopen(url)
      lines = str(openfile.read()).replace('b', '').replace("'", "")
      lines = lines.split("\\n")
      for i in lines:
        print(i)

      def selectRandom(lines):
        return random.choice(lines)

      randomlink = selectRandom(lines)
      frm = frmLink({'link': lines})
      data = frm.save_link()
      print(data, randomlink)
      return JsonResponse({'data': str(randomlink)})

    except Exception as e:
      print(str(e))
      return JsonResponse({'data': str(e)})


class clsSubirFirmas(CreateView):
  template_name = "core/subir_links/subir_firmas.html"
  form_class = frmFile
  success_url = reverse_lazy('subir')


class clsListFirmas(ListView):
  template_name = "core/list_firmas/list_firmas.html"
  model = UserWallet
