from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models, get_user_model
from django.contrib.auth.models import AbstractUser, Group, Permission


class Profile(auth_models.AbstractUser):
    MAX_USERNAME_LEN = 15
    MIN_USERNAME_LEN = 2
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    MIN_PRICE = 1

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        unique=True,
        blank=False,
        null=False,
        validators=(
            validators.MinLengthValidator(MIN_USERNAME_LEN, message="The username must be a minimum of 2 chars"),
        )
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
        )
    )

    email = models.EmailField(
        blank=False,
        null=False
    )

    age = models.IntegerField(
        blank=False,
        null=False,
        validators=(
                       validators.MinValueValidator(18),
        ))

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None
