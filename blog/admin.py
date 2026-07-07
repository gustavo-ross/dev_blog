from django.contrib import admin
from .models import Categoria, Artigo, MensagemContato

admin.site.register(Categoria)

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'data_publicacao')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('categoria', 'data_publicacao')

admin.site.register(MensagemContato)