from django.db import models

class ParametroTiempo(models.Model):
    nombre = models.CharField(max_length=100)
    tiempo = models.DurationField()
    def __str__(self):
        return self.nombre

class BancoDePreguntas(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_preguntas = models.IntegerField(default=0)
    parametro_tiempo = models.ForeignKey(ParametroTiempo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    descripcion = models.TextField()
    ruta = models.CharField(max_length=255, blank=True, null=True)
    banco = models.ForeignKey(BancoDePreguntas, on_delete=models.CASCADE, related_name='preguntas')

    def __str__(self):
        return self.descripcion


class Respuesta(models.Model):
    descripcion = models.CharField(max_length=255)
    correcta = models.BooleanField(default=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')

    def __str__(self):
        return f"{self.descripcion} ({'Correcta' if self.correcta else 'Incorrecta'})"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.correo}"


class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    estudiantes = models.ManyToManyField(Estudiante, related_name='grupos')

    def __str__(self):
        return self.nombre


class Prueba(models.Model):
    titulo = models.CharField(max_length=150)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    numero_preguntas = models.IntegerField(null=True, blank=True)
    banco_preguntas = models.ForeignKey(BancoDePreguntas, on_delete=models.CASCADE, related_name='pruebas', null=True, blank=True)
    grupos = models.ManyToManyField(Grupo, related_name='pruebas')

    def __str__(self):
        return self.titulo
