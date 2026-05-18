from django.shortcuts import render, get_object_or_404
from .models import Videojuego

def home(request):
    busqueda = request.GET.get('buscar')
    if busqueda:
        juegos = Videojuego.objects.filter(titulo__icontains=busqueda)
    else:
        juegos = Videojuego.objects.all()
    return render(request, 'catalogo/index.html', {'juegos': juegos, 'busqueda': busqueda})

def detalle(request, juego_id):
    juego = get_object_or_404(Videojuego, pk=juego_id)
    return render(request, 'catalogo/detalle_juego.html', {'juego': juego})