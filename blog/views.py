from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Categoria
from .forms import ContatoForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ArtigoSerializer, CategoriaSerializer

ARTIGOS_POR_PAGINA = 5

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

    noticias = noticias.order_by('-data_publicacao')

    paginator = Paginator(noticias, ARTIGOS_POR_PAGINA)
    pagina_atual = paginator.get_page(request.GET.get('page'))

    # O botão "Ver mais" busca essa mesma view via fetch() e só precisa da
    # lista de cards nova para anexar no DOM, sem recarregar a página.
    if request.headers.get('X-Requested-With') == 'fetch':
        resposta = render(request, 'blog/partials/artigo_cards.html', {'lista_artigos': pagina_atual})
        resposta['X-Has-Next'] = 'true' if pagina_atual.has_next() else 'false'
        resposta['X-Next-Page'] = str(pagina_atual.next_page_number()) if pagina_atual.has_next() else ''
        return resposta

    # As categorias do menu precisam carregar sempre
    categorias = Categoria.objects.all()

    contexto = {
        'lista_artigos': pagina_atual,
        'page_obj': pagina_atual,
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
        'form': formulario,
        'lista_categorias': Categoria.objects.all(),
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_criar_artigo(request):
    serializer = ArtigoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)