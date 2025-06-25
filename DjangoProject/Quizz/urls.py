from django.contrib import admin
from django.urls import path
from quizz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),

    # Vista después del login
    path('pruebas/', views.seleccionar_prueba, name='seleccionar_prueba'),

    # Iniciar una prueba seleccionada
    path('jugar/iniciar/<int:prueba_id>/', views.iniciar_juego, name='iniciar_juego'),

    # Mostrar pregunta actual
    path('jugar/', views.jugar, name='jugar'),

    # Procesar respuesta
    path('responder/<int:pregunta_id>/', views.responder, name='responder'),

    # Resultado final
    path('resultado/', views.resultado, name='resultado'),

    # Salir del juego (limpiar sesión)
    path('salir/', views.salir, name='salir'),
]
