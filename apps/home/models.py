from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Bank(models.Model):
    
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=100)
    codigo_ispb = models.IntegerField()

    def __self__(self):
        return self.codigo

class Provider(models.Model):

    codigo = models.IntegerField()
    cpf_cnpj = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)

    def __self__(self):
        return self.codigo

class Category(models.Model):

    codigo = models.IntegerField()
    descricao = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1)

    def __self__(self):
        return self.codigo



