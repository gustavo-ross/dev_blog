from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Categoria
from .forms import ContatoForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArtigoSerializer, CategoriaSerializer

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


def artigo_detalhes(request, id):
    categorias = Categoria.objects.all()
    noticia = get_object_or_404(Artigo, id=id)

    contexto = {
        'lista_categorias': categorias,
        'artigo': noticia
   }
    
    return render(request, 'blog/artigo_detalhes.html', contexto)


def fale_conosco(request):
    if request.method == 'POST':
        formulario = ContatoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
        
    else:
        formulario = ContatoForm()

    contexto = {
        'form': formulario
    }

    return render(request, 'blog/contato.html', contexto)


# API REST #

@api_view(['GET'])
def api_listar_artigos(request):
    artigos = Artigo.objects.all()
    serializer = ArtigoSerializer(artigos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_listar_categorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)