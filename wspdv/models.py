from django.db import models

# Create your models here.

class Produto(models.Model):
    codigo = models.IntegerField("codigo", unique=True, blank=False)
    descricao = models.CharField("descricao", max_length=200, blank=False)
    preco = models.DecimalField("preco", max_digits=19, decimal_places=10, blank=False)