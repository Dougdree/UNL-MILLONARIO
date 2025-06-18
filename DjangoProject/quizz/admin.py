from django.contrib import admin
from .models import (
    BancoDePreguntas, Pregunta, Respuesta,
    Grupo, Estudiante, Prueba
)

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 2

class PreguntaInline(admin.TabularInline):
    model = Pregunta
    extra = 1

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'banco')
    search_fields = ('descripcion',)
    inlines = [RespuestaInline]

class BancoDePreguntasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad_preguntas')
    search_fields = ('nombre',)
    inlines = [PreguntaInline]

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'grupo')
    list_filter = ('grupo',)
    search_fields = ('nombre', 'correo')

class PruebaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'hora_inicio', 'numero_preguntas')
    filter_horizontal = ('grupos',)

admin.site.register(BancoDePreguntas, BancoDePreguntasAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Grupo)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Prueba, PruebaAdmin)
