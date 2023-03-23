from django.urls import path
from . import views
urlpatterns = [
    path("", views.home),
    path("menu", views.menu),
    path("portfolio", views.portfolio),
    path("cadastro", views.cadastro),
    path("motorista", views.motorista),
    path("login", views.login),
    path("pesquisa", views.pesquisa),
    path("teste", views.teste)
]
