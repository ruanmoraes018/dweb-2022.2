from django.shortcuts import render

import os


# from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request, 'login.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def home(request):
    return render(request, 'home.html')


def menu(request):
    exibir_h3 = True  # Ou False, dependendo do que você deseja
    return render(request, 'menu.html', {'exibir_h3': exibir_h3})


def pesquisa(request):
    return render(request, 'pesquisa.html')