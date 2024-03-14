from django.db import models
from django.utils import timezone
from decimal import Decimal
from . import choices

from clientes.models import ClienteModel


class PedidosModel(models.Model):
    cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(default=timezone.now)

    def total(self):
        # Inicializa o total do pedido como zero
        total_pedido = Decimal('0.00')

        # Itera sobre todos os itens do pedido e soma seus subtotais
        for item_pedido in self.itens_pedido.all():
            total_pedido += item_pedido.subtotal()

        return total_pedido

    def __str__(self):
        return f'Pedido do cliente: {self.cliente}'


class ProdutosModel(models.Model):
    produto = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.produto}'


class ItemPedidoModel(models.Model):
    pedido = models.ForeignKey(
        PedidosModel, related_name='itens_pedido', on_delete=models.CASCADE)
    produto = models.ForeignKey(
        ProdutosModel, related_name='itens_produto', on_delete=models.CASCADE)
    referencia = models.CharField(max_length=10, choices=choices.REFERENCIA_CHOICES)
    quantidade = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantidade * self.valor_unitario

    def __str__(self):
        return f'Pedido: {self.pedido} Item do pedido: {self.produto} (Quantidade: {self.quantidade}, Valor unitário: {self.valor_unitario})'
