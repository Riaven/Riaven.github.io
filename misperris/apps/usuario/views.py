from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroUsuario

import json 
from django.http import HttpResponse
from rest_framework import generics
from apps.usuario.serializers import UserSerializer
class RegistroUsuario(CreateView):
    model = User
    template_name = "registration/registrar.html"
    form_class = RegistroUsuario
    success_url = reverse_lazy('rescatado_listar')

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer