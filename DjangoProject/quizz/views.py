from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Prueba, Pregunta, Respuesta
import random

# ------------------------------
# Autenticación
# ------------------------------

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('seleccionar_prueba')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Usuario creado correctamente. Ahora inicia sesión.')
        return redirect('login')

    return render(request, 'register.html')


# ------------------------------
# Flujo del juego
# ------------------------------

@login_required
def seleccionar_prueba(request):
    pruebas = Prueba.objects.all()
    return render(request, 'seleccionar_prueba.html', {'pruebas': pruebas})


@login_required
def iniciar_juego(request, prueba_id):
    prueba = get_object_or_404(Prueba, id=prueba_id)
    preguntas = list(
        Pregunta.objects.filter(banco__preguntas__isnull=False).distinct()
    )[:prueba.numero_preguntas]

    random.shuffle(preguntas)

    request.session['preguntas_ids'] = [p.id for p in preguntas]
    request.session['pregunta_actual'] = 0
    request.session['aciertos'] = 0
    request.session['errores'] = 0

    return redirect('jugar')


@login_required
def jugar(request):
    ids = request.session.get('preguntas_ids', [])
    idx = request.session.get('pregunta_actual', 0)

    if idx >= len(ids):
        return redirect('resultado')

    pregunta = get_object_or_404(Pregunta, id=ids[idx])
    respuestas = list(pregunta.respuestas.all())
    random.shuffle(respuestas)

    return render(request, 'juego.html', {
        'pregunta': pregunta,
        'respuestas': respuestas,
        'numero_actual': idx + 1,
        'total': len(ids)
    })


@login_required
def responder(request, pregunta_id):
    if request.method == 'POST':
        respuesta_id = int(request.POST.get('respuesta_id'))
        respuesta = get_object_or_404(Respuesta, id=respuesta_id)

        # Asegura que los contadores existan
        if 'aciertos' not in request.session:
            request.session['aciertos'] = 0
        if 'errores' not in request.session:
            request.session['errores'] = 0
        if 'puntaje' not in request.session:
            request.session['puntaje'] = 0

        # Actualiza según la respuesta
        if respuesta.correcta:
            request.session['aciertos'] += 1
            request.session['puntaje'] += 100
        else:
            request.session['errores'] += 1

        # Avanza a la siguiente pregunta
        request.session['pregunta_actual'] += 1
        return redirect('jugar')

    return redirect('jugar')


@login_required
def resultado(request):
    aciertos = request.session.get('aciertos', 0)
    errores = request.session.get('errores', 0)
    puntaje = request.session.get('puntaje', 0)

    # Limpia la sesión al final si lo deseas
    request.session['preguntas_ids'] = []
    request.session['pregunta_actual'] = 0
    request.session['aciertos'] = 0
    request.session['errores'] = 0
    request.session['puntaje'] = 0

    return render(request, 'resultado.html', {
        'aciertos': aciertos,
        'errores': errores,
        'puntaje': puntaje
    })



@login_required
def salir(request):
    request.session.flush()
    return redirect('seleccionar_prueba')
