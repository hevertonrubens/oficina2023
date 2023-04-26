from django.db import models

# Create your models here.
class Question(models.Model):
  question_text = models.CharField(max_length = 200)
  pub_date = models.DateTimeField('date published')

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete = models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)


class Usuario(models.Model):
  nome = models.CharField(max_length = 60)
  dataAniversario = models.DateTimeField ('Sua data de Aniversário')
  email = models.EmailField(max_length = 100)
  senha = models.CharField(max_length = 100)
  numeroTel = models.IntegerField(default = 0)

class empreendedor(models.Model):
  nome = models.CharField(max_length = 60)
  idEmpreendedor = models.IntegerField(default = 0)
  email = models.EmailField(max_length = 100)
  senha = models.CharField(max_length = 100)

class produtos(models.Model):
  nome = models.CharField(max_length = 60)
  descricao = models.TextField(max_length = 100)
  preço = models.IntegerField(max_length = 100)

class loja(models.Model):
  razaoSocial = models.CharField(max_length = 60)
  cnpj = models.IntegerField (default = 0)