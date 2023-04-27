from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from .models import Passageiro, Motorista, RotaViagem, DiaSemana
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission
from django.utils.translation import gettext_lazy as _

# Passageiros

class PassageiroFormPadrao(UserCreationForm):
    email = forms.EmailField(required=True)
    nome_completo = forms.CharField(max_length=180, label='Nome Completo')
    nome_preferencia = forms.CharField(max_length=50, label='Apelido')
    cpf = forms.CharField(max_length=11, validators=[
        RegexValidator(r'^\d{11}$', 'CPF deve conter 11 dígitos numéricos')
    ])
    telefone = forms.CharField(max_length=20)
    cep = forms.CharField(max_length=8)
    logradouro = forms.CharField(max_length=100)
    numero_residencia = forms.CharField(max_length=10, label='Nº')
    bairro = forms.CharField(max_length=50)
    cidade = forms.CharField(max_length=50)
    estado = forms.CharField(max_length=2)

    class Meta:
        model = User and Passageiro
        fields = ('nome_completo', 'nome_preferencia', 'cpf', 'telefone', 'cep', 'logradouro', 'numero_residencia', 'bairro', 'cidade', 'estado', 'username', 'email')

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data['email']
        if commit:
            usuario.save()
        return usuario

# Motoritas

class MotoristaFormPadrao(UserCreationForm):
    email = forms.EmailField(required=True)
    nome_completo = forms.CharField(max_length=180, label='Nome Completo')
    nome_preferencia = forms.CharField(max_length=50, label='Apelido')
    cpf = forms.CharField(max_length=11, validators=[
        RegexValidator(r'^\d{11}$', 'CPF deve conter 11 dígitos numéricos')
    ])
    telefone = forms.CharField(max_length=20)
    cep = forms.CharField(max_length=8)
    logradouro = forms.CharField(max_length=100)
    numero_residencia = forms.CharField(max_length=10, label='Nº')
    bairro = forms.CharField(max_length=50)
    cidade = forms.CharField(max_length=50)
    estado = forms.CharField(max_length=2)
    cnh = forms.CharField(max_length=11)
    placa = forms.CharField(max_length=7)
    renavam = forms.CharField(max_length=11)
    chassi = forms.CharField(max_length=17)

    class Meta:
        model = User and Motorista
        fields = ('nome_completo', 'nome_preferencia', 'cpf', 'telefone', 'cep', 'logradouro', 'numero_residencia', 'bairro', 'cidade', 'estado', 'cnh', 'placa', 'renavam', 'chassi', 'username', 'email')

    def save(self, commit=True):
        motorista = super().save(commit=False)
        motorista.email = self.cleaned_data['email']
        if commit:
            motorista.save()
        return motorista

# Continuando Usuário

class PassageiroFormPersonalizado(forms.ModelForm):
    is_superuser = forms.BooleanField(
        label=_('Administrador'),
        widget=forms.RadioSelect(choices=((True, _('Sim')), (False, _('Não')))),
        initial=False,
        required=False
    )

    class Meta:
        model = User and Passageiro
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PassageiroFormPersonalizado, self).__init__(*args, **kwargs)
        if self.instance.is_superuser:
            self.fields['is_superuser'].initial = True
        else:
            self.fields['is_superuser'].initial = False
        self.fields['is_superuser'].label = _('Administrador')


# Continuando Motorista

class MotoristaFormPersonalizado(forms.ModelForm):
    is_superuser = forms.BooleanField(
        label=_('Administrador'),
        widget=forms.RadioSelect(choices=((True, _('Sim')), (False, _('Não')))),
        initial=False,
        required=False
    )

    class Meta:
        model = User and Motorista
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MotoristaFormPersonalizado, self).__init__(*args, **kwargs)
        if self.instance.is_superuser:
            self.fields['is_superuser'].initial = True
        else:
            self.fields['is_superuser'].initial = False
        self.fields['is_superuser'].label = _('Administrador')


class LoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'type': 'email'}))
    password = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

# METODO QUE FUNFA

from django import forms
from .models import RotaViagem, DiaSemana


class RotaViagemForm(forms.ModelForm):
    dias_semana = forms.MultipleChoiceField(choices=DiaSemana.DIAS_SEMANA_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = RotaViagem
        fields = ['origem', 'destino', 'horario_ida', 'horario_volta', 'dias_semana']

