from django.db import models

# Create your models here.
class usuario(models.Model):
    Cod_Pro = models.CharField(max_length=40, null=True)
    Descricao = models.CharField(max_length=40, null=True)

    def __str__(self)-> str:
        return self.Cod_Pro

