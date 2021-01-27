from django.shortcuts import render
from .serializers import UsuarioSerializer, TarefaSerializer
from .models import Usuario, Tarefa
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from rest_framework import mixins

class UsuarioList(generics.ListCreateAPIView):    
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TarefaList(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class TarefaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class TarefaUsuario(APIView):

    def get_object(self, fk):
        try:
            tarefa = Tarefa.objects.filter(user=fk)
            return tarefa
        except Tarefa.DoesNotExist:
            raise Http404

    def get(self, request, fk, format=None):
        tarefa = self.get_object(fk)
        serializer = TarefaSerializer(tarefa, many=True)
        return Response(serializer.data)
