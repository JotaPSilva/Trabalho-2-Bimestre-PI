from django.db import models


class MarcaCarro(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey(MarcaCarro, on_delete=models.CASCADE)
    descricao = models.TextField()
    foto = models.ImageField(upload_to="carros/", blank=True, null=True)

    def __str__(self):
        return self.modelo
