from rest_framework import viewsets
from .serializers import PassageiroSerializer, MotoristaSerializer
from .models import Passageiro, Motorista
class PassageiroViewSet(viewsets.ModelViewSet):
    model = Passageiro
    serializer_class = PassageiroSerializer
    queryset = Passageiro.objects.all()
    filter_fields = ('user', 'nome_completo', 'nome_preferencia', 'cpf', 'telefone', 'cep', 'logradouro', 'numero_residencia', 'bairro', 'cidade', 'estado', 'username', 'email', 'password')
class MotoristaViewSet(viewsets.ModelViewSet):
    model = Motorista
    serializer_class = MotoristaSerializer
    queryset = Motorista.objects.all()
    filter_fields = ('user', 'nome_completo', 'nome_preferencia', 'cpf', 'telefone', 'cep', 'logradouro', 'numero_residencia', 'bairro', 'cidade', 'estado', 'cnh', 'placa', 'renavam', 'chassi', 'username', 'email', 'password')