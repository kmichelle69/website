from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser
from localflavor.us.models import PhoneNumberField

class NewUser(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    phone = PhoneNumberField()
    address = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    # is_active = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
