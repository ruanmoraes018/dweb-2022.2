from rest_framework import serializers
from .models import Passageiro, Motorista, Custom
from rolepermissions.roles import assign_role
class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = ['nome_completo', 'nome_preferencia', 'cpf', 'telefone', 'cep', 'logradouro', 'numero_residencia', 'bairro', 'cidade', 'estado', 'cnh', 'placa', 'renavam', 'chassi', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': True},
            'is_staff': {'read_only': False},
            'is_superuser': {'read_only': False},
            'user_permissions': {'read_only': True},
            'groups': {'read_only': True},}
    def create(self, validated_data):
        custom_data = {
            'email': validated_data['email'],
            'username': validated_data['username']}
        custom = Custom.objects.create(**custom_data)
        password = validated_data.pop('password')
        motorista = Motorista.objects.create(user=custom, **validated_data)
        custom.set_password(password)
        motorista.set_password(password)
        custom.save()
        motorista.save()
        assign_role(motorista, 'motorista')
        return motorista
class PassageiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passageiro
        fields = ['nome_completo', 'nome_preferencia', 'cpf', 'telefone', 'cep', 'logradouro', 'numero_residencia', 'bairro', 'cidade', 'estado', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': True},
            'is_staff': {'read_only': False},
            'is_superuser': {'read_only': False},
            'user_permissions': {'read_only': True},
            'groups': {'read_only': True},}    
    def create(self, validated_data):
        custom_data = {
            'email': validated_data['email'],
            'username': validated_data['username']}
        custom = Custom.objects.create(**custom_data)
        password = validated_data.pop('password')
        passageiro = Passageiro.objects.create(user=custom, **validated_data)
        custom.set_password(password)
        passageiro.set_password(password)
        custom.save()
        passageiro.save()
        assign_role(passageiro, 'passageiro')
        return passageiro