from django.urls import path, include
from rest_framework import routers
from .viewset import PassageiroViewSet, MotoristaViewSet
from . import views
router = routers.DefaultRouter()
router.register(r'passageiro', PassageiroViewSet, basename="Passageiro")
router.register(r'motorista', MotoristaViewSet, basename="Motorista")
urlpatterns = [
    path("", views.home, name='página inicial'),
    path("menu", views.menu, name='menu'),
    path("portfolio", views.portfolio, name='portfolio'),
    path("cadastro/passageiro", views.cadastro_passageiro, name='cadastro_passageiro'),
    path("cadastro/motorista", views.cadastro_motorista, name='cadastro_motorista'),
    path('login/motorista', views.login_motorista, name='login_motorista'),
    path('motorista', views.menu_motorista, name='menu_motorista'),
    path('passageiro', views.menu_passageiro, name='menu_passageiro'),
    path('login/passageiro', views.login_passageiro, name='login_passageiro'),
    path('logout/', views.logout_view, name='logout'),
    path("página/motorista", views.pagina_motorista, name='pagina_motorista'),
    path("página/passageiro", views.pagina_passageiro, name='pagina_passageiro'),
    path("pesquisa", views.pesquisa, name='pesquisa'),
    path("resultados-busca0", views.resultados0, name='resultados0'),
    path("resultados-busca1", views.resultados1, name='resultados1'),
    path('rotas/criar', views.criar_rota, name='criar_rota'),
    path('rotas/visualizar', views.lista_rotas, name='lista_rotas'),
    path('rotas/atualizar_rota/<int:id>/', views.atualizar_rota, name='atualizar_rota'),
    path('rotas/deletar_rota/<int:id>/', views.deletar_rota, name='deletar_rota'),
    path('api/', include(router.urls)),
    path('termos_uso/', views.termos, name='termos'),
]
