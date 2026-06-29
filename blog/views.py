from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'blog/index.html')


def sobre_nos(request):
    mensagem = "<h1>Sobre o Devblog!</h1> <p>Ainda nem existe, então não tem muito o que falar.</p>"

    return HttpResponse(mensagem)