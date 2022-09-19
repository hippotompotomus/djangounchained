from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Breed(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, 'Breed must be longer than 2 characters')]
        )
    def __str__(self):
        return self.name

class Cat(models.Model):
    nickname = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, 'Nickname must be longer than 2 chatacters')]
        )
    weight = models.PositiveIntegerField(default=20)
    foods = models.CharField(max_length=200)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname