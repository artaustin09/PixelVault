from django.shortcuts import render, get_object_or_404
from .models import Videojuego

def home(request):
    juegos = Videojuego.objects.all()
    # Verifica que el archivo esté en templates/catalogo/home.html
    return render(request, 'catalogo/home.html', {'juegos': juegos})

def detalle_juego(request, juego_id):
    juego = get_object_or_404(Videojuego, pk=juego_id)
    return render(request, 'catalogo/detalle_juego.html', {'juego': juego})

def confirmar_compra(request, juego_id):
    juego = get_object_or_404(Videojuego, pk=juego_id)
    return render(request, 'catalogo/confirmacion.html', {'juego': juego})