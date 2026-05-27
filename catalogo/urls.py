from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('juego/<int:juego_id>/', views.detalle_juego, name='detalle_juego'),
    
    # Rutas del Carrito
    path('carrito/', views.ver_carrito, name="ver_carrito"),
    path('agregar/<int:juego_id>/', views.agregar_al_carrito, name="agregar_al_carrito"),
    path('eliminar/<int:juego_id>/', views.eliminar_del_carrito, name="eliminar_del_carrito"),
    path('limpiar/', views.limpiar_carrito, name="limpiar_carrito"),
    
    # Confirmación (Ruta fija sin ID)
    path('confirmar-compra/', views.confirmar_compra, name="confirmar_compra"),
]