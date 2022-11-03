from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

#------------------------------------------------------------------------------
class Bank(models.Model):
    
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=40)
    codigo_ispb = models.IntegerField()

    def __self__(self):
        return self

#------------------------------------------------------------------------------
class Provider(models.Model):

    codigo = models.IntegerField()
    cpf_cnpj = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=40)
    nome_fantasia = models.CharField(max_length=40)
    telefone = models.CharField(max_length=14)

    def __self__(self):
        return self.razao_social

#------------------------------------------------------------------------------
class Category(models.Model):

    codigo = models.IntegerField()
    descricao = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1)

    def __self__(self):
        return self.descricao

#------------------------------------------------------------------------------
class BankAccount(models.Model):

    codigo = models.IntegerField()
    codigo_banco = models.IntegerField()
    descricao = models.CharField(max_length=40)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    conta_dv = models.IntegerField()
    tipo_conta = models.CharField(max_length=20)

    def __self__(self):
        return self.descricao

#------------------------------------------------------------------------------
class Budgets(models.Model):

    codigo = models.IntegerField()
    descricao = models.CharField(max_length=40)
    codigo_categoria = models.IntegerField()
    codigo_banco = models.IntegerField()
    codigo_fornecedor = models.IntegerField()
    valor_estimado = models.fields.DecimalField(max_digits=14, decimal_places=2)
    valor_acumulado = models.fields.DecimalField(max_digits=14, decimal_places=2)
    data_inicio = models.DateField()
    data_final = models.DateField()
    data_prevista = models.DateField()

    def __self__(self):
        return self.descricao

#------------------------------------------------------------------------------
class BillsToPay(models.Model):

    codigo = models.IntegerField()
    descricao = models.CharField(max_length=40)
    codigo_categoria = models.IntegerField()
    codigo_banco = models.IntegerField()
    codigo_fornecedor = models.IntegerField()
    valor_a_pagar = models.fields.DecimalField(max_digits=14, decimal_places=2)
    valor_pago = models.fields.DecimalField(max_digits=14, decimal_places=2)
    juros = models.fields.DecimalField(max_digits=14, decimal_places=2)
    data_entrada = models.DateField()
    data_pagamento = models.DateField()
    data_prevista = models.DateField()

    def __self__(self):
        return self.descricao

#------------------------------------------------------------------------------
class Receipts(models.Model):

    codigo = models.IntegerField()
    descricao = models.CharField(max_length=40)
    codigo_categoria = models.IntegerField()
    codigo_banco = models.IntegerField()
    codigo_fornecedor = models.IntegerField()
    valor_a_pagar = models.fields.DecimalField(max_digits=14, decimal_places=2)
    valor_pago = models.fields.DecimalField(max_digits=14, decimal_places=2)
    juros = models.fields.DecimalField(max_digits=14, decimal_places=2)
    data_entrada = models.DateField()
    data_pagamento = models.DateField()
    data_prevista = models.DateField()

    def __self__(self):
        return self.descricao