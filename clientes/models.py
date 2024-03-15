from django.db import models


class ClienteModel(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    telefone = models.IntegerField()
    fantasia = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nome} - Cidade: {self.cidade}'