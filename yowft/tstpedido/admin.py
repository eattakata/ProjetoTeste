from django.contrib import admin
from .models import Cliente, Contato, Endereco, Especie, Categoria, Produto, Pedido, ItensPedido, Unidade, Preco


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Contato)
admin.site.register(Endereco)
admin.site.register(Especie)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(ItensPedido)
admin.site.register(Unidade)
admin.site.register(Preco)
