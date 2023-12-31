from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


#Change EmailBackend to UsernameBackend since email is not in use anymore
class UsernameBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
