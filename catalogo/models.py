from django.db import models

class Desarrolladora(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    def __str__(self): return self.nombre

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50) # Ej: PS5, Xbox, PC
    fabricante = models.CharField(max_length=50)
    def __str__(self): return self.nombre

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=50) # Gamertag del vendedor
    def __str__(self): return self.nombre