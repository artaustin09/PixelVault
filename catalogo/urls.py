from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('juego/<int:juego_id>/', views.detalle_juego, name='detalle_juego'),
    path('confirmar-compra/<int:juego_id>/', views.confirmar_compra, name='confirmar_compra'),
]