from django.contrib import admin
from . import models


admin.site.register(models.PedidosModel)
admin.site.register(models.ProdutosModel)
admin.site.register(models.ItemPedidoModel)

