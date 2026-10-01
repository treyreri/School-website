from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        PARENT = 'PARENT', 'Родитель'
        STUDENT = 'STUDENT', 'Ученик'
        MANAGER = 'MANAGER', 'Менеджер'
        ADMIN = 'ADMIN', 'Администратор'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    phone = models.CharField(
    max_length=30,
    blank=True,
    )

    school_class = models.ForeignKey(
        'main.Class',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
    )

    def __str__(self):
        return self.username