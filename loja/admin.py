from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'preco', 'estoque')
    list_filter = ('tipo',)
    search_fields = ('nome', 'descricao')
