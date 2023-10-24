# Generated by Django 4.2.6 on 2023-10-24 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0010_alter_review_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='creditos',
            field=models.ManyToManyField(blank=True, to='movieApp.actor'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='estudio',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='movieApp.estudio'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='fechaEstreno',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='generos',
            field=models.ManyToManyField(blank=True, to='movieApp.genero'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='pais',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
