from rolepermissions.roles import AbstractUserRole
class Passageiro(AbstractUserRole):
    available_permissions = {'ver_rotas': True}
class Motorista(AbstractUserRole):
    available_permissions = {'cadastrar_rotas': True}