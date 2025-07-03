from django.contrib import admin
from .models import (
    BancoDePreguntas, Pregunta, Respuesta,
    Grupo, Estudiante, Prueba, ParametroTiempo
)

# ------------------------------
# Inlines
# ------------------------------

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 2

class PreguntaInline(admin.TabularInline):
    model = Pregunta
    extra = 1

# ------------------------------
# Admin personalizados
# ------------------------------

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'banco')
    search_fields = ('descripcion',)
    inlines = [RespuestaInline]

class BancoDePreguntasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad_preguntas')
    search_fields = ('nombre',)
    inlines = [PreguntaInline]

class ParametroTiempoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tiempo')
    search_fields = ('nombre',)

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo')
    search_fields = ('nombre', 'correo')

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    filter_horizontal = ('estudiantes',)  # Muestra selector múltiple en el admin

class PruebaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'hora_inicio', 'numero_preguntas')
    filter_horizontal = ('grupos',)

# ------------------------------
# Registro
# ------------------------------

admin.site.register(BancoDePreguntas, BancoDePreguntasAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ParametroTiempo, ParametroTiempoAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Prueba, PruebaAdmin)
