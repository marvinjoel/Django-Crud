from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from crud.forms import UsuarioForm
from crud.models import UsuarioModel


class UsuarioList(ListView):

    model = UsuarioModel
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Usuarios'
        return context



class UsuarioCreate(CreateView):

    model = UsuarioModel
    form_class = UsuarioForm
    template_name = 'create.html'
    success_url = reverse_lazy('list')

class UsuarioUpdate(UpdateView):

    model = UsuarioModel
    form_class = UsuarioForm
    template_name = 'create.html'
    success_url = reverse_lazy('list')

class UsuarioDelete(DeleteView):
    model = UsuarioModel
    template_name = 'delete.html'
    success_url = reverse_lazy('list')
