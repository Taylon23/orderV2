from django.urls import path
from . import views



urlpatterns = [
    path('pedidos/',views.ListarPedidos.as_view(), name='listar-pedidos'),
    path('adicionar/', views.AdicionarPedido.as_view(), name='adicionar-pedido'),
    path('editar/<int:pk>/', views.EditarPedido.as_view(), name='editar-pedido'),
    path('excluir/<int:pk>/', views.ExcluirPedido.as_view(), name='excluir-pedido'),
    
    path('produtos/', views.ListarProdutos.as_view(), name='listar-produtos'),
    path('adicionar-produto/', views.AdicionarProduto.as_view(), name='adicionar-produto'),
    path('editar-produto/<int:pk>/', views.EditarProduto.as_view(), name='editar-produto'),
    path('excluir-produto/<int:pk>/', views.ExcluirProduto.as_view(), name='excluir-produto'),
    
    path('itens_pedido/<int:pedido_id>/', views.itens_pedido, name='itens-pedido'),
    path('item_pedido/criar/', views.ItemPedidoCreateView.as_view(), name='adicionar-item-pedido'),
    path('item_pedido/<int:pk>/editar/', views.ItemPedidoUpdateView.as_view(), name='editar-item-pedido'),
    path('item_pedido/<int:pk>/excluir/', views.ItemPedidoDeleteView.as_view(), name='excluir-item-pedido'),
    path('item_pedido/<int:pedido_id>/imprimir/', views.imprimir_pedido, name='imprimir-item-pedido'), 
]