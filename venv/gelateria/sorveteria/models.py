from django.db import models

# Create your models here.
class Sabores(models.Model):
    nomes_sabor = models.CharField(max_length = 200)
    fotos_sabor = models.CharField(max_length = 200)
    descricao_sabor = models.CharField(max_length = 500)

    def __str__(self) -> str:
        return self.nomes_sabor

