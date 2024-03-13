from django import forms
from .models import PedidosModel, ProdutosModel


class PedidoForm(forms.ModelForm):
    class Meta:
        model = PedidosModel
        fields = ['cliente']
        
class ProdutoForm(forms.ModelForm):
        
    class Meta:
        model = ProdutosModel
        fields = '__all__'
        
    
        
