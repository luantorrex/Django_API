from rest_framework import serializers, viewsets
from empresa.models import Funcionario
from empresa.serializer import FuncionarioSerializer

class FuncionariosViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
