from .models import *
from django.forms import *


class frmFile(ModelForm):
  class Meta:
    model = PoapLink
    fields = '__all__'


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
