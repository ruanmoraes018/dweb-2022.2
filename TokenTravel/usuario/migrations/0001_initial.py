# Generated by Django 4.2 on 2023-06-25 03:12

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import usuario.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_motorista', models.BooleanField(default=False)),
                ('is_passageiro', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DiaSemana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='motorista', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Nome de Usuário')),
                ('nome_completo', models.CharField(max_length=180, verbose_name='Nome Completo')),
                ('nome_preferencia', models.CharField(max_length=50, verbose_name='Apelido')),
                ('cnh', models.CharField(max_length=11, unique=True, verbose_name='CNH')),
                ('cpf', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^\\d{11}$', 'CPF deve conter 11 dígitos numéricos')], verbose_name='CPF')),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('placa', models.CharField(max_length=10)),
                ('renavam', models.CharField(max_length=11)),
                ('chassi', models.CharField(max_length=17)),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=100)),
                ('numero_residencia', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('is_active', models.BooleanField(default=True, verbose_name='Está Ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='É Pessoal?')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Administrador')),
                ('groups', models.ManyToManyField(blank=True, related_name='motoristas', to='auth.group', verbose_name='grupos')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Permissões específicas para este usuário.', related_name='motoristas', related_query_name='motorista', to='auth.permission', verbose_name='permissões do usuário')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', usuario.models.MotoristaManager()),
            ],
        ),
        migrations.CreateModel(
            name='RotaViagem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('origem', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('horario_ida', models.TimeField()),
                ('tipo_veiculo', models.CharField(max_length=50)),
                ('dias_semana', models.ManyToManyField(to='usuario.diasemana')),
                ('motorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.motorista')),
            ],
        ),
        migrations.CreateModel(
            name='Passageiro',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Nome de Usuário')),
                ('nome_completo', models.CharField(max_length=180, verbose_name='Nome Completo')),
                ('nome_preferencia', models.CharField(max_length=50, verbose_name='Apelido')),
                ('cpf', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^\\d{11}$', 'CPF deve conter 11 dígitos numéricos')], verbose_name='CPF')),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=100)),
                ('numero_residencia', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('is_active', models.BooleanField(default=True, verbose_name='Está Ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='É Pessoal?')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Administrador')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='passageiros', to='auth.group', verbose_name='grupos')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Permissões específicas para este usuário.', related_name='passageiros', related_query_name='passageiro', to='auth.permission', verbose_name='permissões do usuário')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
