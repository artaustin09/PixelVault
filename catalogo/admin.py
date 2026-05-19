from django.contrib import admin
from .models import Desarrolladora, Plataforma, Vendedor, Videojuego, Cliente, Venta, Genero # Agregamos Genero aquí

admin.site.register(Desarrolladora)
admin.site.register(Plataforma)
admin.site.register(Vendedor)
admin.site.register(Videojuego)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Genero) # Registramos la nueva tabla aquí