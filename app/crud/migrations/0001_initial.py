# Generated by Django 3.1.5 on 2021-02-22 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('Asname', models.CharField(max_length=200, verbose_name='Apellido')),
                ('Age', models.IntegerField(verbose_name='Edad')),
                ('Profetion', models.CharField(max_length=50, verbose_name='Profeción')),
                ('Photo', models.ImageField(blank=True, max_length=350, null=True, upload_to='static/usuarios/', verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['id'],
            },
        ),
    ]
