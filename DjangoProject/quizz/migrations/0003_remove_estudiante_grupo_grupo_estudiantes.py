# Generated by Django 5.2.3 on 2025-06-25 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0002_grupo_rename_es_correcta_respuesta_correcta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='grupo',
        ),
        migrations.AddField(
            model_name='grupo',
            name='estudiantes',
            field=models.ManyToManyField(related_name='grupos', to='quizz.estudiante'),
        ),
    ]
