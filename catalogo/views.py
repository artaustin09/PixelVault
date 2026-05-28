from django.shortcuts import render, get_object_or_404, redirect
from .models import Videojuego
from .carrito import Carrito 
from django.db.models import Q # Para el buscador avanzado
from django.contrib.auth import login
from .forms import RegistroForm
# --- HOME CON BUSCADOR PROFUNDO ---
def home(request):
    juegos = Videojuego.objects.all()
    query = request.GET.get('buscar')
    
    if query:
        # Buscamos por Título, Géneros, Desarrolladora o Vendedor
        # NOTA: He quitado 'plataforma' de la búsqueda automática para evitar el FieldError
        # si no estamos seguros del nombre del campo.
        juegos = juegos.filter(
            Q(titulo__icontains=query) | 
            Q(generos__nombre__icontains=query) |
            Q(desarrolladora__nombre__icontains=query) |
            Q(vendedor__nombre__icontains=query)
        ).distinct()
        
    return render(request, 'catalogo/home.html', {
        'juegos': juegos,
        'busqueda': query
    })

# --- DETALLE DEL JUEGO (CORREGIDO PARA EVITAR FIELDERROR) ---
def detalle_juego(request, juego_id):
    # Traemos el juego con TODAS sus relaciones
    juego = get_object_or_404(
        Videojuego.objects.select_related('desarrolladora', 'vendedor').prefetch_related('plataformas', 'generos'), 
        pk=juego_id
    )
    return render(request, 'catalogo/detalle_juego.html', {'juego': juego})

# --- FUNCIONES DEL CARRITO (Mantenlas igual) ---
def agregar_al_carrito(request, juego_id):
    carrito = Carrito(request)
    juego = get_object_or_404(Videojuego, id=juego_id)
    carrito.agregar(juego=juego)
    return redirect("home")

def ver_carrito(request):
    return render(request, 'catalogo/carrito_detalle.html')

def eliminar_del_carrito(request, juego_id):
    carrito = Carrito(request)
    juego = get_object_or_404(Videojuego, id=juego_id)
    carrito.eliminar(juego)
    return redirect("ver_carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("ver_carrito")

def confirmar_compra(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'catalogo/confirmacion.html')

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Inicia sesión automáticamente al registrarse
            return redirect("home")
    else:
        form = RegistroForm()
    return render(request, "catalogo/registro.html", {"form": form})