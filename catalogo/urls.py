from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('juego/<int:juego_id>/', views.detalle, name='detalle'),
]