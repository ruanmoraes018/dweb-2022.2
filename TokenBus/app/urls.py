# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#    path('admin/', admin.site.urls),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("menu", views.menu),
    path("cadastro", views.cadastro),
    path("login", views.login),
    path("pesquisa", views.pesquisa)
]
