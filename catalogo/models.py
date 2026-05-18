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

class Videojuego(models.Model):
    titulo = models.CharField(max_length=150)
    desarrolladora = models.ForeignKey(Desarrolladora, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    portada = models.ImageField(upload_to='juegos/', null=True, blank=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)
    def __str__(self): return f"{self.titulo} ({self.plataforma})"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    gamertag = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    def __str__(self): return self.nombre

class Venta(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_compra = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self): return f"{self.cliente} compró {self.videojuego}"
