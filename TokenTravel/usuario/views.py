from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import RotaViagem, DiaSemana
from .forms import RotaViagemForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Motorista, Passageiro, Custom, RotaViagem
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.http.response import HttpResponse
from rolepermissions.roles import assign_role
from django.contrib.auth.hashers import make_password

import django
django.setup()


def cadastro_motorista(request):
    if request.method == 'POST':
        # Recupere os dados do formulário
        username = request.POST.get('username')
        nome_completo = request.POST.get('nome_completo')
        nome_preferencia = request.POST.get('nome_preferencia')
        cnh = request.POST.get('cnh')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        placa = request.POST.get('placa')
        renavam = request.POST.get('renavam')
        chassi = request.POST.get('chassi')
        cep = request.POST.get('cep')
        logradouro = request.POST.get('logradouro')
        numero_residencia = request.POST.get('numero_residencia')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        password = request.POST.get('senha')
        # Crie um novo objeto Usuario com os dados do formulário

        novo_user = Custom.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_motorista=True
        )

        novo_motorista = Motorista(
            user=novo_user,
            username=username,
            email=email,
            password=make_password(password),
            nome_completo=nome_completo,
            nome_preferencia=nome_preferencia,
            cnh=cnh,
            cpf=cpf,
            telefone=telefone,
            placa=placa,
            renavam=renavam,
            chassi=chassi,
            cep=cep,
            logradouro=logradouro,
            numero_residencia=numero_residencia,
            bairro=bairro,
            cidade=cidade,
            estado=estado,
        )
        novo_motorista.save()

        assign_role(novo_motorista, 'motorista')

        # Redirecione para a página de sucesso
        messages.success(request, 'Cadastro realizado com sucesso!')
        return HttpResponse('Sucesso Motorista!')

    # Se a requisição não for POST, renderize o template do formulário de cadastro de motorista
    return render(request, 'cadastro_motoristas.html')

# Cadastro de Passageiros


def cadastro_passageiro(request):
    if request.method == 'POST':
        # Recupere os dados do formulário
        username = request.POST.get('username')
        nome_completo = request.POST.get('nome_completo')
        nome_preferencia = request.POST.get('nome_preferencia')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        cep = request.POST.get('cep')
        logradouro = request.POST.get('logradouro')
        numero_residencia = request.POST.get('numero_residencia')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        password = request.POST.get('senha')
        # Crie um novo objeto Usuario com os dados do formulário
        novo_usuario = Custom.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_passageiro=True
        )
        # Crie um novo objeto Passageiro com os dados do formulário
        novo_passageiro = Passageiro(
            user=novo_usuario,
            username=username,
            email=email,
            password=make_password(password),
            nome_completo=nome_completo,
            nome_preferencia=nome_preferencia,
            cpf=cpf,
            telefone=telefone,
            cep=cep,
            logradouro=logradouro,
            numero_residencia=numero_residencia,
            bairro=bairro,
            cidade=cidade,
            estado=estado
        )
        novo_passageiro.save()

        assign_role(novo_passageiro, 'passageiro')

        # Redirecione para a página de sucesso
        messages.success(request, 'Cadastro realizado com sucesso!')
        return HttpResponse('Sucesso Passageiro!')

    # Se a requisição não for POST, renderize o template do formulário de cadastro de passageiro
    return render(request, 'cadastro_usuarios.html')


def login_motorista(request):
    if request.method == "GET":
        return render(request, 'login_motorista.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('senha')

        # autenticando o usuário com o autenticador personalizado
        user = authenticate(request, email=email, password=password,
                            backend='usuario.backends.MotoristaBackend')

        if user is not None:
            if user.is_active and hasattr(user, 'motorista'):
                login(request, user)
                return redirect(pagina_motorista)
            else:
                messages.error(
                    request, 'Este usuário não é um motorista cadastrado.')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'login_motorista.html')

# Login de Passageiro


def login_passageiro(request):
    if request.method == "GET":
        return render(request, 'login_usuario.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('senha')

        # autenticando o usuário com o autenticador personalizado
        passageiro = authenticate(
            request, email=email, password=password, backend='usuario.backends.PassageiroBackend')

        if passageiro is not None:
            if passageiro.is_active and hasattr(passageiro, 'passageiro'):
                login(request, passageiro)
                return HttpResponse('Irineu')
            else:
                messages.error(
                    request, 'Este usuário não é um passageiro cadastrado.')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'login_usuario.html')


# METODO QUE FUNFA


@login_required(login_url='login/motorista')
def criar_rota(request):
    if request.method == 'POST':
        form = RotaViagemForm(request.POST)
        if form.is_valid():
            rota = form.save(commit=False)
            rota.motorista = request.user.motorista
            horario_ida_str = form.cleaned_data['horario_ida'].strftime(
                '%Y-%m-%dT%H:%M:%S%z')
            horario_volta_str = form.cleaned_data['horario_volta'].strftime(
                '%Y-%m-%dT%H:%M:%S%z')
            rota.horario_ida = datetime.fromisoformat(horario_ida_str)
            rota.horario_volta = datetime.fromisoformat(horario_volta_str)
            rota.save()  # salva rota no banco de dados para obter um id
            dias_semana = form.cleaned_data['dias_semana']
            for dia_nome in dias_semana:
                dia, _ = DiaSemana.objects.get_or_create(nome=dia_nome)
                rota.dias_semana.add(dia)
            messages.success(request, "Rota cadastrada com sucesso!")
            return redirect(lista_rotas)
    else:
        form = RotaViagemForm()
    return render(request, 'criar_rota.html', {'form': form})


# @login_required(login_url='login/motorista')
# def criar_rota(request):
#     if request.method == 'POST':
#         # recupera os dados do formulário
#         origem = request.POST.get('origem')
#         destino = request.POST.get('destino')
#         preco = request.POST.get('preco')
#         horario_ida = request.POST.get('horario_ida')
#         horario_volta = request.POST.get('horario_volta')
#         dias_semana = request.POST.get('dias_semana')
#         ida_volta = request.POST.get('ida_volta') == 'on'

#         # cria um novo objeto Rota de Viagem com os dados do formulário
#         nova_rota = RotaViagem(
#             motorista=request.user.motorista,
#             origem=origem,
#             destino=destino,
#             preco=preco,
#             horario_ida=horario_ida,
#             horario_volta=horario_volta,
#             dias_semana=dias_semana,
#             ida_volta=ida_volta
#         )
#         nova_rota.save()

#         # redireciona para a página de sucesso
#         messages.success(request, 'Rota criada com sucesso!')
#         return HttpResponseRedirect(reverse('lista_rotas'))

    # se a requisição não for POST, renderiza o template do formulário de criação de rota
    # return render(request, 'criar_rota.html')


@login_required(login_url='login/motorista')
def lista_rotas(request):
    rotas = RotaViagem.objects.filter(motorista=request.user.motorista)
    return render(request, 'lista_rotas.html', {'rotas': rotas})


# @login_required(login_url='login/motorista')
# def atualizar_rota(request, id):
#     rota = get_object_or_404(RotaViagem, id=id)
#     if request.method == 'POST':
#         form = RotaViagemForm(request.POST or None, request.FILES or None, instance=rota)
#         if form.is_valid():
#             rota = form.save(commit=False)
#             dias_semana = form.cleaned_data['dias_semana']
#             rota.dias_semana.clear()
#             for dia in dias_semana:
#                 if dia.isdigit():
#                     rota.dias_semana.add(int(dia))
#             rota.save()
#             return redirect(lista_rotas)
#         else:
#             form = RotaViagemForm(instance=rota)
#     return render(request, 'atualizar_rota.html', {'form': form, 'rota': rota})


@login_required(login_url='login/motorista')
def atualizar_rota(request, id):
    rota = get_object_or_404(RotaViagem, id=id)
    if request.method == 'POST':
        form = RotaViagemForm(request.POST or None, request.FILES or None, instance=rota)
        if form.is_valid():
            rota = form.save(commit=False)
            rota.motorista = request.user.motorista
            horario_ida_str = form.cleaned_data['horario_ida'].strftime('%Y-%m-%dT%H:%M:%S%z')
            horario_volta_str = form.cleaned_data['horario_volta'].strftime('%Y-%m-%dT%H:%M:%S%z')
            rota.horario_ida = datetime.fromisoformat(horario_ida_str)
            rota.horario_volta = datetime.fromisoformat(horario_volta_str)
            rota.save()
            dias_semana = form.cleaned_data['dias_semana']
            rota.dias_semana.clear()
            for dia_nome in dias_semana:
                dia, _ = DiaSemana.objects.get_or_create(nome=dia_nome)
                rota.dias_semana.add(dia)
            messages.success(request, "Rota atualizada com sucesso!")
            return redirect('lista_rotas')
    else:
        form = RotaViagemForm(instance=rota)
    return render(request, 'atualizar_rota.html', {'form': form, 'rota': rota})


@login_required(login_url='login/motorista')
def deletar_rota(request, pk):
    rota = get_object_or_404(RotaViagem, pk=pk, motorista=request.user.motorista)

    # Verifica se a rota possui dias da semana associados a ela
    if rota.dias_semana.exists():
        # Cria uma cópia da lista de dias da semana da rota
        dias_semana = list(rota.dias_semana.all())
        # Remove todos os objetos da lista sem afetar outras rotas
        for dia in dias_semana:
            dia.delete()

    # Deleta a rota
    rota.delete()

    # redireciona para a página de sucesso
    messages.success(request, 'Rota deletada com sucesso!')
    return HttpResponseRedirect(reverse(lista_rotas))



@login_required(login_url='login/motorista')
def menu_motorista(request):
    motorista = request.user.motorista
    rotas = RotaViagem.objects.filter(motorista=motorista)
    return render(request, 'menu_motorista.html', {'motorista': motorista, 'rotas': rotas})


@login_required(login_url='login')
def pagina_restrita_passageiro(request):
    return HttpResponse('Bora Bill, PS!')


def logout_view(request):
    logout(request)
    return redirect(menu)

def portfolio(request):
    return render(request, 'portfolio.html')

def home(request):
    return render(request, 'home.html')

def menu(request):
    exibir_h3 = True  # Ou False, dependendo do que você deseja
    return render(request, 'menu.html', {'exibir_h3': exibir_h3})

def pesquisa(request):
    return render(request, 'pagina_motorista.html')

@login_required(login_url='login/motorista')
def pagina_motorista(request):
    return render(request, 'pagina_motorista.html')