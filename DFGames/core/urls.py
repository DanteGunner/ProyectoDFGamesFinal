from django.contrib import admin
from django.urls import path, include
from .views import home, playstation, xbox, switch, comprar, formulario, listar_juegos, eliminar_juego, modificar_juego

urlpatterns = [
    path('', home, name='home'),
    path('playstation/', playstation, name='playstation'),
    path('xbox/', xbox, name='xbox'),
    path('switch/', switch, name='switch'),
    path('formulario/', formulario, name='formulario'),
    path('comprar/', comprar, name='comprar'),
    path('listar-juegos/', listar_juegos, name='listado_juegos'),
    path('eliminar-juego/<id>/', eliminar_juego, name='eliminar_juego'),
    path('modificar-juego/<id>/', modificar_juego, name='modificar_juego'),
    path('accounts/', include('django.contrib.auth.urls')),
]
