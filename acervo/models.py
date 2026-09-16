from django.db import models

# Create your models here.
class LivroDigital(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    
class LivroFisico(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo