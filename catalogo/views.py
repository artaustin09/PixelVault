from django.shortcuts import render, get_object_or_404
from .models import Videojuego

def home(request):
    juegos = Videojuego.objects.all()
    # Buscador opcional
    query = request.GET.get('q')
    if query:
        juegos = juegos.filter(titulo__icontains=query)
    return render(request, 'catalogo/index.html', {'juegos': juegos})

def detalle(request, juego_id):
    # Trae el juego o lanza error 404 si el ID no existe
    juego = get_object_or_404(Videojuego, pk=juego_id)
    return render(request, 'catalogo/detalle_juego.html', {'juego': juego})