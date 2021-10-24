from .models import *
from django.forms import *


class frmFile(ModelForm):
  class Meta:
    model = PoapLink
    fields = '__all__'

    widgets = {
      'linkpoap': ClearableFileInput(
        attrs={
          'class': 'form-control-file mt-3'
        }
      )
    }


class frmLink(ModelForm):
  class Meta:
    model = Link
    fields = '__all__'

  def save_link(self, commit=True):
    data = {}
    form = super()
    try:
      if form.is_valid():
        instance = form.save()
        data = instance
      else:

        data['error'] = form.errors
    except Exception as e:
      print("No valido")
      data['error'] = str(e)
    return data


class frmUserWallet(ModelForm):
  class Meta:
    model = UserWallet
    fields = '__all__'

    widgets = {
      'img': TextInput(
        attrs={
          'class': 'form-control',
          'placeholder': 'Ingrese su NickName',
          'id': 'txtNickName',
        }
      ),
      'name': TextInput(
        attrs={
          'class': 'form-control',
          'placeholder': 'Ingrese su NickName',
          'id': 'txtNickName',
        }
      ),
      'wallet_address': TextInput(
        attrs={
          'class': 'form-control',
          'placeholder': 'Ingrese la dirección de su wallet',
          'readonly': '',
          'id': 'txtWalletAddress',
        }
      ),
      'firma': TextInput(
        attrs={
          'class': 'form-control',
          'placeholder': 'Ingrese la firma',
          'readonly': '',
          'id': 'txtFirma',
        }
      ),
    }
