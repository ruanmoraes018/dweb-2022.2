from django.shortcuts import render


# from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def homepage(request):
    return render(request, 'home.html')


def menu(request):
    return render(request, 'menu.html')


def pesquisa(request):
    return render(request, 'pesquisa.html')


