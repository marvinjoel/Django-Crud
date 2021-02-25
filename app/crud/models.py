from django.db import models

class UsuarioModel(models.Model):


    Name = models.CharField(verbose_name='Nombre', max_length=200)
    Asname = models.CharField(verbose_name='Apellido', max_length=200)
    Age = models.IntegerField(verbose_name='Edad')
    Profetion = models.CharField(verbose_name='Profeción', max_length=50)
    Photo = models.ImageField(upload_to='static/usuarios/', max_length=350, verbose_name='Foto', blank=True, null=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']
