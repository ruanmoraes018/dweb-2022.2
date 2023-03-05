from django.shortcuts import render


# from django.http import HttpResponse


# Create your views here.
def start(request):
    return render(request, 'test.html')
    # HttpResponse("Meu primeiro response html em django")


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


