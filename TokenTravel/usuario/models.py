from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


class Custom(AbstractUser):
    is_motorista = models.BooleanField(default=False)
    is_passageiro = models.BooleanField(default=False)


class PassageiroManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        passageiro = Passageiro(user=user, **extra_fields)
        passageiro.user = user
        passageiro.save()
        return user


class Passageiro(AbstractBaseUser, PermissionsMixin):
    user = models.OneToOneField(
        Custom, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(
        max_length=50, unique=True, verbose_name='Nome de Usuário')
    nome_completo = models.CharField(
        max_length=180, verbose_name='Nome Completo')
    nome_preferencia = models.CharField(max_length=50, verbose_name='Apelido')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF', validators=[
        RegexValidator(r'^\d{11}$', 'CPF deve conter 11 dígitos numéricos')])
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    cep = models.CharField(max_length=8, verbose_name='CEP')
    logradouro = models.CharField(max_length=100)
    numero_residencia = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    is_active = models.BooleanField(default=True, verbose_name='Está Ativo?')
    is_staff = models.BooleanField(default=False, verbose_name='É Pessoal?')
    is_superuser = models.BooleanField(
        default=False, verbose_name='Administrador')
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = PassageiroManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    groups = models.ManyToManyField(Group, verbose_name=_(
        'grupos'), blank=True, related_name='passageiros')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('permissões do usuário'),
        blank=True,
        help_text=_('Permissões específicas para este usuário.'),
        related_name='passageiros',
        related_query_name='passageiro',)

    def __str__(self):
        return self.nome_preferencia


class MotoristaManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O Email é obrigatório')
        email = self.normalize_email(email)
        user = Custom.objects.create_user(email=email, password=password)
        motorista = self.model(user=user, **extra_fields)
        motorista.save(using=self._db)
        return motorista


class Motorista(AbstractBaseUser, PermissionsMixin):
    user = models.OneToOneField(
        Custom, on_delete=models.CASCADE, related_name='motorista', primary_key=True)
    username = models.CharField(
        max_length=50, unique=True, verbose_name='Nome de Usuário')
    nome_completo = models.CharField(
        max_length=180, verbose_name='Nome Completo')
    nome_preferencia = models.CharField(max_length=50, verbose_name='Apelido')
    cnh = models.CharField(max_length=11, unique=True, verbose_name='CNH')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF', validators=[
        RegexValidator(r'^\d{11}$', 'CPF deve conter 11 dígitos numéricos')])
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    placa = models.CharField(max_length=10)
    renavam = models.CharField(max_length=11)
    chassi = models.CharField(max_length=17)
    cep = models.CharField(max_length=8, verbose_name='CEP')
    logradouro = models.CharField(max_length=100)
    numero_residencia = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    is_active = models.BooleanField(default=True, verbose_name='Está Ativo?')
    is_staff = models.BooleanField(default=False, verbose_name='É Pessoal?')
    is_superuser = models.BooleanField(
        default=False, verbose_name='Administrador')
    objects = MotoristaManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    groups = models.ManyToManyField(Group, verbose_name=_(
        'grupos'), blank=True, related_name='motoristas')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('permissões do usuário'),
        blank=True,
        help_text=_('Permissões específicas para este usuário.'),
        related_name='motoristas',
        related_query_name='motorista',)

    def __str__(self):
        return self.username


class DiaSemana(models.Model):
    nome = models.CharField(max_length=20)
    DIAS_SEMANA_CHOICES = [
        ('domingo', 'Dom'),
        ('segunda', 'Seg'),
        ('terca', 'Ter'),
        ('quarta', 'Qua'),
        ('quinta', 'Qui'),
        ('sexta', 'Sex'),
        ('sabado', 'Sáb'),]

    def __str__(self):
        return self.nome


class RotaViagem(models.Model):
    id = models.AutoField(primary_key=True)
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    horario_ida = models.TimeField()
    dias_semana = models.ManyToManyField(DiaSemana)
    tipo_veiculo = models.CharField(max_length=50)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)

    def __str__(self):
        if self.tipo_veiculo:
            return f"Viagem (ida) de {self.motorista.nome_preferencia} de {self.origem} para {self.destino} - Partida: {self.horario_ida.strftime('%H:%M')}"
        else:
            return f"Viagem (ida) de {self.motorista.nome_preferencia} de {self.origem} para {self.destino} - Partida: {self.horario_ida.strftime('%H:%M')}"

    def save(self, *args, **kwargs):
        form_data = kwargs.pop('form_data', None)
        super(RotaViagem, self).save(*args, **kwargs)
        if form_data:
            self.dias_semana.clear()
            for dia in form_data.get('dias_semana'):
                dia_obj = DiaSemana.objects.get_or_create(nome=dia)
                self.dias_semana.add(dia_obj)
