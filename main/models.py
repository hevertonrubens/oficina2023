from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=60)
    data_aniversario = models.DateTimeField('Data de Aniversário')
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    numero_tel = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


class Empreendedor(models.Model):
    nome = models.CharField(max_length=60)
    id_empreendedor = models.IntegerField(default=0)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.TextField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome


class Loja(models.Model):
    razao_social = models.CharField(max_length=60)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.razao_social
