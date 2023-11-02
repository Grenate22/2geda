from .models import User
from django.contrib.auth.backends import ModelBackend


class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if '@' in username:  # Check if username is an email
                user = User.objects.get(email=username)
            elif username.isdigit():  # Check if username is a number, assuming it's a phone number
                user = User.objects.get(phone_number=username)
            else:
                user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
