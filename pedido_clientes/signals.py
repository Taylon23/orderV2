# signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import ProdutosModel


# Funcao para salvar pruduto com primeira letra maiusculua
@receiver(pre_save, sender=ProdutosModel)
def capitalize_first_letter(sender, instance, **kwargs):
    instance.produto = instance.produto.capitalize()
