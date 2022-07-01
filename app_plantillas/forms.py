from django import forms

class FormAnimal(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaAnimal(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)