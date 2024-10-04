from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.managers import UserManager


class CustomUser(AbstractUser):
    phone = PhoneNumberField(unique=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []  # Email va boshqa maydonlar talab qilinmaydi
    objects = UserManager()

    def __str__(self):
        return str(self.phone)
