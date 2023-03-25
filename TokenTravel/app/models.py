from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.db import models

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=180)
    nome_preferencia = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True, validators=[
        RegexValidator(r'^\d{11}$', 'CPF deve conter 11 dígitos numéricos')
    ])
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    logradouro = models.CharField(max_length=100)
    numero_residencia = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    password = models.CharField(max_length=20, validators=[
        MinLengthValidator(8, 'Senha deve conter no mínimo 8 caracteres'),
        MaxLengthValidator(20, 'Senha deve conter no máximo 20 caracteres')
    ])
    def __str__(self):
        return self.nome_preferencia
