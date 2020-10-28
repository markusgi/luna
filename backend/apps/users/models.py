from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)
    username = models.CharField(
        verbose_name='username',
        max_length=200,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=200,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=200,
        blank=True,
    )
    location = models.CharField(
        verbose_name='location',
        max_length=200,
        blank=True,
    )
    phone = PhoneField(
        blank=True,
        help_text='Contact phone number'
    )
    things_love = models.CharField(
        blank=True,
        max_length=200,
    )
    description = models.CharField(
        blank=True,
        max_length=200
    )
    date_joined = models.DateTimeField(
        auto_now_add=True
    )
    profile_picture = models.ImageField(
        upload_to='',
        blank=True
    )

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
