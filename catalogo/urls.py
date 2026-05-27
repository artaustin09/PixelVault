from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Detalle del juego (Cambiado de uuid a int)
    path('juego/<int:juego_id>/', views.detalle_juego, name='detalle_juego'),

    # Rutas del Carrito (Todas con <int:juego_id>)
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:juego_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:juego_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
    path('confirmar-compra/', views.confirmar_compra, name='confirmar_compra'),

    # Autenticación
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='catalogo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]