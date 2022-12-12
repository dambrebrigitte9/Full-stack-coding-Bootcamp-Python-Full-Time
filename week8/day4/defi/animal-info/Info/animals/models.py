from django.db import models


# Create your models here.
class animals(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    legs = models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    weight = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'

class person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    phone_number = models.Field(max_length=30)
    address= models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'
