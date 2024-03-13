from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from . import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import forms
from django.db.models.functions import Lower 


def clientes_view(request):
    clientes = models.ClienteModel.objects.all().order_by(Lower('nome'))
    return render(request, 'clientes.html', {"clientes": clientes})


class AdicionarCliente(CreateView):
    form_class = forms.ClienteForm
    template_name = 'form_cliente.html'
    success_url = reverse_lazy('clientes-tabela')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = 'Adicionar'
        return context


class EditarCliente(UpdateView):
    model = models.ClienteModel
    form_class = forms.ClienteForm
    template_name = 'form_cliente.html'
    success_url = reverse_lazy('clientes-tabela')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button'] = 'Editar'
        return context


def excluir_cliente(request, pk):
    cliente = get_object_or_404(models.ClienteModel, pk=pk)
    
    if request.method == 'POST':
        # Se o método for POST, significa que o formulário de confirmação foi enviado
        cliente.delete()
        return redirect('clientes-tabela')  # Redireciona para a página de clientes após a exclusão
        
    return render(request, 'form_excluir_cliente.html', {'cliente': cliente})
    
