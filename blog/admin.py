from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html

from .models import Categoria, Artigo, MensagemContato

admin.site.site_header = "UXBlog Admin"
admin.site.site_title = "UXBlog Admin"
admin.site.index_title = "Painel de administração"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'total_artigos')
    search_fields = ('nome',)
    ordering = ('nome',)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(_total_artigos=Count('artigo'))

    @admin.display(description='Artigos', ordering='_total_artigos')
    def total_artigos(self, obj):
        return obj._total_artigos


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('miniatura', 'titulo', 'autor', 'categoria', 'data_publicacao')
    list_display_links = ('miniatura', 'titulo')
    search_fields = ('titulo', 'conteudo', 'autor')
    list_filter = ('categoria', 'data_publicacao')
    ordering = ('-data_publicacao',)
    list_per_page = 25
    autocomplete_fields = ('categoria',)

    @admin.display(description='Imagem')
    def miniatura(self, obj):
        if obj.imagem:
            return format_html('<img class="thumbnail-preview" src="{}" alt="">', obj.imagem.url)
        return '—'


@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio')
    search_fields = ('nome', 'email', 'mensagem')
    ordering = ('-data_envio',)
    readonly_fields = ('nome', 'email', 'mensagem', 'data_envio')

    def has_add_permission(self, request):
        return False
