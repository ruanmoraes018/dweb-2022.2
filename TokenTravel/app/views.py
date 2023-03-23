from django.shortcuts import render, redirect
from .models import Usuario
import os


# from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request, 'login.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def cadastro(request):
    if request.method == 'POST':
        novo_usuario = Usuario(
            nome_completo=request.POST.get('nome_completo'),
            nome_preferencia=request.POST.get('nome_preferencia'),
            cpf=request.POST.get('cpf'),
            telefone=request.POST.get('telefone'),
            email=request.POST.get('email'),
            cep=request.POST.get('cep'),
            logradouro=request.POST.get('logradouro'),
            numero_residencia=request.POST.get('numero_residencia'),
            bairro=request.POST.get('bairro'),
            cidade=request.POST.get('cidade'),
            estado=request.POST.get('estado'),
            senha=request.POST.get('senha'),
        )
        novo_usuario.save()
        return redirect(teste)# redireciona para uma página de sucesso
    return render(request, 'cadastro-usuarios.html')


def teste(request):
    return render(request, 'teste.html')


def motorista(request):
    return render(request, 'cadastro-motoristas.html')


def home(request):
    return render(request, 'home.html')


def menu(request):
    exibir_h3 = True  # Ou False, dependendo do que você deseja
    return render(request, 'menu.html', {'exibir_h3': exibir_h3})


def pesquisa(request):
    return render(request, 'pesquisa.html')


