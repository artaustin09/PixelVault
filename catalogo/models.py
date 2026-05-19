from django.db import models

class Desarrolladora(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    
    def __str__(self): 
        return self.nombre

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50) # Ej: PS5, Xbox Series X, Nintendo Switch, PC
    fabricante = models.CharField(max_length=50)
    
    def __str__(self): 
        return self.nombre

# --- NUEVA TABLA DE GÉNEROS ---
class Genero(models.Model):
    nombre = models.CharField(max_length=50) # Ej: Acción, RPG, Deportes, Shooter
    
    def __str__(self): 
        return self.nombre

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=50) # Gamertag del vendedor
    
    def __str__(self): 
        return self.nombre

class Videojuego(models.Model):
    titulo = models.CharField(max_length=150)
    # CORREGIDO: Ortografía correcta de 'desarrolladora'
    desarrolladora = models.ForeignKey(Desarrolladora, on_delete=models.CASCADE) 
    
    # RELACIÓN 1 (Muchos a Muchos): Un juego puede estar en varias consolas
    plataformas = models.ManyToManyField(Plataforma) 
    
    # RELACIÓN 2 (Muchos a Muchos): Un juego puede tener múltiples géneros
    generos = models.ManyToManyField(Genero, blank=True)
    
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    portada = models.ImageField(upload_to='juegos/', null=True, blank=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)
    
    def __str__(self): 
        return self.titulo

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    gamertag = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    
    def __str__(self): 
        return self.nombre

class Venta(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_compra = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self): 
        return f"{self.cliente} compró {self.videojuego}"