from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'blog/index.html')


def sobre_nos(request):
    return render(request, 'blog/sobre.html')