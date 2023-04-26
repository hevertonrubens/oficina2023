from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.

def index(request):
  questoes = Question.objects.all()
  context = {
    'questoes_template':questoes
  }
  return render(request, 'index.html', context)

def detail(request, question_id):
  questao = Question.objects.get(id = question_id)
  opcoes = Choice.objects.filter(question = question_id)
  context = {
    'pergunta': questao,
    'respostas': opcoes
  }
  return render(request, 'detail.html', context)

def results(request, question_id):
  questao = Question.objects.get(id = question_id)
  opcoes = Choice.objects.filter(question = question_id)
  context = {
    'pergunta': questao,
    'respostas': opcoes
  }
  return render (request, 'results.html', context)

def vote(request, question_id):
  if request.method == 'POST':
    post = request.POST
    opcao_votada = Choice.objects.get(id = post ['voto'])
    opcao_votada.votes = opcao_votada.votes + 1
    opcao_votada.save()
  questao = Question.objects.get(id = question_id)
  opcoes = Choice.objects.filter(question = question_id)
  context = {
    'pergunta': questao,
    'respostas': opcoes
  }
  return render (request, 'vote.html', context)

# def detail(request, question_id):
#   return HttpResponse("Hello, Details.")

# def results(request, question_id):
#   response = "Essa é a pagina de reusultados da questão %s."
#   return HttpResponse(response % question_id)

# def vote (request, question_id):
#   return HttpResponse("Esta é a página de votação da questão %s." % question_id)

# def index(request):
#   return HttpResponse("Hello, world. You're at the polls index.")
# def contact(request):
#   return HttpResponse("Hello, Contact")