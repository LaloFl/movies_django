# Generated by Django 4.2.6 on 2023-10-23 07:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0002_remove_pelicula_encines_pelicula_pais_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(max_length=200)),
                ('calificacion', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieApp.pelicula')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieApp.usuario')),
            ],
        ),
    ]
