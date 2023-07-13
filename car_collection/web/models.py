from django.core import validators, exceptions
from django.db import models


class Car(models.Model):
    MAX_TYPE_LEN = 10
    MAX_SPEED_LEN = 10
    MAX_SPEED = 500
    MIN_SPEED = 1
    MAX_MODEL_LEN = 20
    MIN_MODEL_LEN = 2
    MIN_PRICE = 1
    MIN_YEAR = 1980
    MAX_YEAR = 2049

    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CARS = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER)
    )

    type = models.CharField(
        max_length=MAX_TYPE_LEN,
        blank=False,
        null=False,
        choices=CARS,
    )

    model = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_MODEL_LEN,
        validators=(
            validators.MinLengthValidator(MIN_MODEL_LEN),
        )
    )
    speed = models.IntegerField(
        blank=True,
        null=True,
        validators=(
            validators.MaxValueValidator(MAX_SPEED),
            validators.MinValueValidator(MIN_SPEED),
        )
    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            validators.MaxValueValidator(MAX_YEAR, "Year must be between 1980 and 2049"),
            validators.MinValueValidator(MIN_YEAR, "Year must be between 1980 and 2049"),
        )
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=(
            validators.MinValueValidator(MIN_PRICE),
        )
    )
