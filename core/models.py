from django.db import models

# Create your models here.
class Carro(models.Model):
    tipo = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    marca  =models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    preco = models.FloatField()
    ano = models.DateField()
    km = models.FloatField()
    pagamento = models.FloatField()
    leilao = models.BooleanField()
    
    
    def __str__(self):
        return super().__str__()
    
    
