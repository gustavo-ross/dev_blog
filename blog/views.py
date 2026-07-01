from django.http import HttpResponse
from django.shortcuts import render
from .models import Artigo, Categoria

def home(request):
    # Captura o ID da categoria pela URL (ex: /?categoria=1)
    categoria_id = request.GET.get('categoria')
    
    # Se existe um ID na URL, filtramos. Se não, mostramos tudo.
    if categoria_id:
        noticias = Artigo.objects.filter(categoria_id=categoria_id)
        # Pegamos a categoria específica para mandar para o título
        categoria_atual = Categoria.objects.filter(id=categoria_id).first()
    else:
        noticias = Artigo.objects.all()
        categoria_atual = None

    # As categorias do menu precisam carregar sempre
    categorias = Categoria.objects.all()
    
    contexto = {
        'lista_artigos': noticias,
        'lista_categorias': categorias,
        'categoria_atual': categoria_atual, # Enviamos a categoria filtrada para o HTML
    }
    return render(request, 'blog/index.html', contexto)


def sobre_nos(request):
    # Para o menu dinâmico aparecer na página Sobre, a view também precisa enviar os dados!
    categorias = Categoria.objects.all()
    contexto = {
        'lista_categorias': categorias
    }
    return render(request, 'blog/sobre.html', contexto)