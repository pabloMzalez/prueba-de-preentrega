from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion = models.DateTimeField(null=True)
    
    def __str__(self):
        return f"Soy un objeto llamado {self.nombre} de {self.edad} años"