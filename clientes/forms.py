from django import forms
from .models import ClienteModel


class ClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteModel
        fields = ['nome', 'cidade', 'telefone', 'fantasia']
