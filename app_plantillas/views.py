from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Animal

# Create your views here.

def vista1(request):
    return HttpResponse("hola")

def vista2(request):
    
    plantilla1= loader.get_template("plantilla1.html")
    render = plantilla1.render({})
    return HttpResponse(render)

def vista3(request):
    # una forma de hacerlo apra entender el proceso
    # plantilla_for = loader.get_template("plantilla_for.html")
    
    animal1 = Animal(nombre= "JUAN")    
    animal2 = Animal(nombre= "pedro")
    animal3 = Animal(nombre= "jose")
    animal1.save()
    animal2.save()
    animal3.save()
    
    # render = plantilla_for.render({"lista_animal": [animal1, animal2, animal3]})
    # return HttpResponse(render)
    # forma correcta
    return render(request, "plantilla_for.html", {"lista_animal": [animal1, animal2, animal3]} )