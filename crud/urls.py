
from django.urls import path
from crud.views import UsuarioList, UsuarioCreate, UsuarioUpdate, UsuarioDelete

urlpatterns = [
    path('', UsuarioList.as_view(), name='list'),
    path('create/', UsuarioCreate.as_view(), name='create'),
    path('update/<int:pk>', UsuarioUpdate.as_view(), name='update'),
    path('delete/<int:pk>', UsuarioDelete.as_view(), name='delete'),
]
