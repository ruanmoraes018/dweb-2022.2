from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path("admin", admin.site.urls),
    path("", views.home, name='página inicial'),
    path("menu", views.menu, name='menu'),
    path("portfolio", views.portfolio, name='portfolio'),
    path("cadastro_usuario", views.cadastro_usuario, name='cadastro/usuario'),
    path('login', views.login, name='login'),
    path("motorista", views.motorista, name='motorista'),
    path("pesquisa", views.pesquisa, name='pesquisa'),
    path("teste", views.teste, name='teste')
]
