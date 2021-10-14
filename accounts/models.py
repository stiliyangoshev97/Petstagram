from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.db import models

from accounts.managers import PetstagramUserManager




# Creating managers


# Extending user model
class PetstagramUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,)
    # In users model we will find the is_staff and is_superuser attributes above
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True,)


    USERNAME_FIELD = "email"
    #  Overriding objects (managers) so we can access admin-panel with email address
    #  and be able to create a superuser
    objects = PetstagramUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(blank=True, upload_to='profiles')
    user = models.OneToOneField(PetstagramUser, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

# Importing signals so the profile gets created automatically
from accounts.signals import user_created