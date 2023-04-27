from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='página inicial'),
    path("menu", views.menu, name='menu'),
    path("portfolio", views.portfolio, name='portfolio'),
    path("cadastro/passageiro", views.cadastro_passageiro, name='cadastro_passageiro'),
    path("cadastro/motorista", views.cadastro_motorista, name='cadastro_motorista'),
    path('login/motorista', views.login_motorista, name='login_motorista'),
    path('motorista', views.menu_motorista, name='menu_motorista'),
    path('login/passageiro', views.login_passageiro, name='login_passageiro'),
    path('logout/', views.logout_view, name='logout'),
    path("página/motorista", views.pagina_motorista, name='pagina_motorista'),
    path("pesquisa", views.pesquisa, name='pesquisa'),
    path('rotas/criar', views.criar_rota, name='criar_rota'),
    path('rotas/visualizar', views.lista_rotas, name='lista_rotas'),
    path('atualizar_rota/<int:id>/', views.atualizar_rota, name='atualizar_rota'),
    path('deletar_rota/<int:pk>', views.deletar_rota, name='deletar_rota'),
]
