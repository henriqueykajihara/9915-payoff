from socket import fromshare
from django import forms
from .models import *

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = [ 'codigo', 'cpf_cnpj', 'razao_social', 'nome_fantasia' ]

        