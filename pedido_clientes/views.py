from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PedidosModel, ProdutosModel, ItemPedidoModel
from .forms import PedidoForm, ProdutoForm

# Listagem de pedidos


class ListarPedidos(ListView):
    model = PedidosModel
    template_name = 'listar_pedidos.html'
    context_object_name = 'pedidos'
    
    def get_queryset(self):
        return PedidosModel.objects.all().order_by('cliente')


# Adicionar pedido


class AdicionarPedido(CreateView):
    model = PedidosModel
    form_class = PedidoForm
    template_name = 'form_pedido.html'
    success_url = reverse_lazy('listar-pedidos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = 'Adicionar'
        return context

# Editar pedido


class EditarPedido(UpdateView):
    model = PedidosModel
    form_class = PedidoForm
    template_name = 'form_pedido.html'
    success_url = reverse_lazy('listar-pedidos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = 'Editar'
        return context

# Excluir pedido


class ExcluirPedido(DeleteView):
    model = PedidosModel
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('listar-pedidos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = 'Deletar'
        context['title'] = 'Excluir Pedido'
        return context


# Listagem de produtos


class ListarProdutos(ListView):
    model = ProdutosModel
    template_name = 'listar_produtos.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        return ProdutosModel.objects.all().order_by('produto')

# Adicionar produto


class AdicionarProduto(CreateView):
    model = ProdutosModel
    form_class = ProdutoForm
    template_name = 'form_produto.html'
    success_url = reverse_lazy('listar-produtos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = 'Adicionar'
        return context

# Editar produto


class EditarProduto(UpdateView):
    model = ProdutosModel
    form_class = ProdutoForm
    template_name = 'form_produto.html'
    success_url = reverse_lazy('listar-produtos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = 'Editar'
        return context

# Excluir produto


class ExcluirProduto(DeleteView):
    model = ProdutosModel
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('listar-produtos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = 'Deletar'
        context['title'] = 'Excluir Protudo'
        return context


def itens_pedido(request, pedido_id):
    pedido = get_object_or_404(PedidosModel, id=pedido_id)
    itens_pedido = ItemPedidoModel.objects.filter(pedido=pedido)
    return render(request, 'listar_items_pedido.html', {'pedido': pedido, 'itens_pedido': itens_pedido})


class ItemPedidoCreateView(CreateView):
    model = ItemPedidoModel
    fields = '__all__'
    template_name = 'form_item_pedido.html'

    def get_success_url(self):
        # Obtém o ID do pedido a partir dos dados do formulário
        pedido_id = self.object.pedido.id
        # Redireciona de volta à página de detalhes do pedido com o ID do pedido
        return reverse_lazy('itens-pedido', kwargs={'pedido_id': pedido_id})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['produto'].queryset = form.fields['produto'].queryset.order_by(
            'produto')
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = 'Adicionar'
        return context


class ItemPedidoUpdateView(UpdateView):
    model = ItemPedidoModel
    fields = '__all__'
    template_name = 'form_item_pedido.html'
    success_url = reverse_lazy('')

    def get_success_url(self):
        # Obtém o ID do pedido a partir dos dados do formulário
        pedido_id = self.object.pedido.id
        # Redireciona de volta à página de detalhes do pedido com o ID do pedido
        return reverse_lazy('itens-pedido', kwargs={'pedido_id': pedido_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = 'Editar'
        return context


class ItemPedidoDeleteView(DeleteView):
    model = ItemPedidoModel
    template_name = 'form_excluir.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = 'Deletar'
        context['title'] = 'Excluir Item do Pedido'
        return context

    def get_success_url(self):
        # Obtém o ID do pedido a partir dos dados do formulário
        pedido_id = self.object.pedido.id
        # Redireciona de volta à página de detalhes do pedido com o ID do pedido
        return reverse_lazy('itens-pedido', kwargs={'pedido_id': pedido_id})


def imprimir_pedido(request, pedido_id):
    pedido = PedidosModel.objects.get(id=pedido_id)
    itens_pedido = pedido.itens_pedido.all()
    total_pedido = sum(item.subtotal() for item in itens_pedido)
    return render(request, 'imprimir_pedido.html', {'pedido': pedido, 'itens_pedido': itens_pedido, 'total_pedido': total_pedido})
