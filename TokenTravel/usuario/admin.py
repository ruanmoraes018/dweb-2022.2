from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import PassageiroFormPersonalizado, MotoristaFormPersonalizado
from .models import Passageiro, Motorista, Custom, RotaViagem, DiaSemana
admin.site.register(Custom, UserAdmin)


class SuperPassageiro(UserAdmin):
    add_form = PassageiroFormPersonalizado
    form = PassageiroFormPersonalizado
    list_display = ('username', 'email', 'nome_preferencia',
                    'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'nome_preferencia')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Informações Pessoais'), {
         'fields': ('nome_completo', 'nome_preferencia', 'cpf', 'telefone')}),
        (_('Informações de Endereço'), {'fields': (
            'cep', 'logradouro', 'numero_residencia', 'bairro', 'cidade', 'estado')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nome_completo', 'nome_preferencia', 'cpf', 'telefone',
                       'cep', 'logradouro', 'numero_residencia', 'bairro', 'cidade', 'estado', 'is_superuser'),
        }),)


admin.site.register(Passageiro, SuperPassageiro)


class SuperMotorista(UserAdmin):
    add_form = MotoristaFormPersonalizado
    form = MotoristaFormPersonalizado
    list_display = ('username', 'email', 'nome_preferencia',
                    'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'nome_preferencia')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Informações Pessoais'), {
         'fields': ('nome_completo', 'nome_preferencia', 'cpf', 'telefone')}),
        (_('Informações de Endereço'), {'fields': (
            'cep', 'logradouro', 'numero_residencia', 'bairro', 'cidade', 'estado')}),
        (_('Informações de CNH'), {
         'fields': ('cnh', 'placa', 'renavam', 'chassi')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nome_completo', 'nome_preferencia', 'cpf', 'telefone',
                       'cep', 'logradouro', 'numero_residencia', 'bairro', 'cidade', 'estado',
                       'cnh', 'placa', 'renavam', 'chassi', 'is_superuser'),
        }),)


admin.site.register(Motorista, SuperMotorista)


class RotaViagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'origem', 'destino', 'preco',
                    'horario_ida', 'dias_semana_list', 'tipo_veiculo')

    def dias_semana_list(self, obj):
        dias_semana = obj.dias_semana.all()
        if isinstance(dias_semana, DiaSemana):
            dias_semana = [dias_semana]
        return ", ".join([dia.nome for dia in dias_semana])
    dias_semana_list.short_description = 'Dias da semana'


admin.site.register(RotaViagem, RotaViagemAdmin)
