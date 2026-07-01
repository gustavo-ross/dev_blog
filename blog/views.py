from django.http import HttpResponse
from django.shortcuts import render
from .models import Artigo

def home(request):
    noticias = Artigo.objects.all()
    contexto = {
        'lista_artigos': noticias
    }
    return render(request, 'blog/index.html', contexto)


def sobre_nos(request):
    return render(request, 'blog/sobre.html')