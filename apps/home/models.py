from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

###############################################################################
class Bank(models.Model):
    
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=100)
    codigo_ispb = models.IntegerField()

    def __self__(self):
        return self.descricao

class Provider(models.Model):

    codigo = models.IntegerField()
    cpf_cnpj = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)

    def __self__(self):
        return self.razao_social

class Category(models.Model):

    codigo = models.IntegerField()
    descricao = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1)

    def __self__(self):
        return self.descricao

class Budgets(models.Model):

    codigo = models.IntegerField()
    codigo_categoria = models.IntegerField()
    codigo_banco = models.IntegerField()
    codigo_fornecedor = models.IntegerField()
    valor_estimado = models.fields.DecimalField(max_digits=14, decimal_places=2)
    
