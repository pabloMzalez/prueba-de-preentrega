from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=30, null=True)