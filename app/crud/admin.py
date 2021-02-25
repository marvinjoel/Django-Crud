from django.contrib import admin

from app.crud.models import UsuarioModel


@admin.register(UsuarioModel)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Asname','Age','Profetion','Photo']