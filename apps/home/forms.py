from socket import fromshare
from django import forms
from .models import *

#------------------------------------------------------------------------------
class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields =  ['codigo', 'descricao', 'codigo_ispb']

#------------------------------------------------------------------------------
class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = [ 'codigo', 'cpf_cnpj', 'razao_social', 'nome_fantasia' ]

#------------------------------------------------------------------------------
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields =  ['codigo', 'descricao', 'tipo']

#------------------------------------------------------------------------------
class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = [ 'codigo', 'codigo_banco', 'descricao', 'agencia', 'conta', 'conta_dv', 'tipo_conta' ]

#------------------------------------------------------------------------------
class BudgetsForm(forms.ModelForm):
    class Meta:
        model = Budgets
        fields = [ 'codigo', 'descricao', 'codigo_categoria', 'codigo_banco', 'codigo_fornecedor', 'valor_estimado', 'valor_acumulado', 'data_inicio', 'data_final', 'data_prevista' ]
