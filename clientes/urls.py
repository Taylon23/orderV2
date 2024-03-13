from django.urls import path
from . import views

urlpatterns = [
    path('tabela/',views.clientes_view,name='clientes-tabela'),
     path('adicionar/', views.AdicionarCliente.as_view(), name='adicionar-cliente'),
    path('editar/<int:pk>/', views.EditarCliente.as_view(), name='editar-cliente'),
    path('excluir/<int:pk>/', views.excluir_cliente, name='excluir-cliente'),
]