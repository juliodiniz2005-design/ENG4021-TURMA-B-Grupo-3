from django.contrib import admin
from .models import MercadoParceiro, Produto

@admin.register(MercadoParceiro)
class MercadoParceiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'mercado', 'preco_original', 'preco_desconto', 'validade', 'percentual_desconto')
    list_filter = ('mercado', 'validade')
    search_fields = ('titulo',)