from django.forms import *
from django.utils.safestring import mark_safe

from crud.models import UsuarioModel



#Listar todo el formulario
class UsuarioForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class']='form-control'
            form.field.widget.attrs['autocomplete']='off'
        self.fields['Photo'].widget.attrs['class']='form-control'

    class Meta:
        model = UsuarioModel
        fields = ['Name','Asname','Age','Profetion','Photo']

    def render(self, Photo, value, attrs=None):  # pylint: disable=E1002
        output = []
        css = {'style': 'clear:left;float:left;margin:1em 1em 0 0;'}
        output.append(super().render(Photo, value, attrs=css))
        if value and hasattr(value, "url"):
            output.append(('<a target="_blank" href="%s">'
                           '<img src="%s" alt="" '
                           'style="float:left;border:1px solid black;" /></a> '
                           % (value.url, value.url)))
        return mark_safe(u''.join(output))


