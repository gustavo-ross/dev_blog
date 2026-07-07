from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre_nos, name='sobre_nos'),
    path('artigo/<int:id>/', views.artigo_detalhes, name='detalhe_artigo'),
    path('contato/', views.fale_conosco, name="fale_conosco"),

    # APIs #

    path('api/artigos/', views.api_listar_artigos, name='api_artigos'),
    path('api/artigos/novo', views.api_criar_artigo, name='api_criar_artigo'),
    path('api/categorias/', views.api_listar_categorias, name='api_categorias'),
]