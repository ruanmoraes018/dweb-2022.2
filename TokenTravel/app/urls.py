from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path("admin", admin.site.urls),
    path("", views.home),
    path("menu", views.menu),
    path("portfolio", views.portfolio),
    path("cadastro", views.cadastro),
    path("login", views.login),
    path("motorista", views.motorista),
    path("pesquisa", views.pesquisa),
    path("teste", views.teste)
]
