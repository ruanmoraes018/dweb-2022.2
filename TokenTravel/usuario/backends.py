from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class PassageiroBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(
                Q(email=email) & Q(is_passageiro=True))
        except UserModel.DoesNotExist:
            return None
        if user.check_password(password):
            return user

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id, is_active=True, is_passageiro=True)
        except UserModel.DoesNotExist:
            return None


class MotoristaBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(email=email) & Q(is_motorista=True))
        except UserModel.DoesNotExist:
            return None
        if user.check_password(password):
            return user

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id, is_active=True, is_motorista=True)
        except UserModel.DoesNotExist:
            return None
