from datetime import datetime
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app_plantillas.forms import BusquedaAnimal, FormAnimal
from app_plantillas.models import Animal

# Create your views here.

def vista1(request):
    return render(request, "index.html")

def vista2(request):
    
    plantilla1= loader.get_template("plantilla1.html")
    render = plantilla1.render({})
    return HttpResponse(render)

# def vista3(request, nombre):
#     # una forma de hacerlo apra entender el proceso
#     # plantilla_for = loader.get_template("plantilla_for.html")
    
    
#     # animal1 = Animal(nombre= "JUAN")    
#     # animal2 = Animal(nombre= "pedro")
#     # animal3 = Animal(nombre= "jose")
#     # animal1.save()
#     # animal2.save()
#     # animal3.save()
    
#     # # render = plantilla_for.render({"lista_animal": [animal1, animal2, animal3]})
#     # # return HttpResponse(render)
#     # # forma correcta
#     # return render(request, "plantilla_for.html", {"lista_animal": [animal1, animal2, animal3]} )

#     animal = Animal(nombre = nombre) 
#     animal.save()
    
#     lista_animales = Animal.objects.all()
    
#     return render(request, "plantilla_for.html", {"lista_animal": lista_animales})

def crear_animal(request):
    
    if request.method == "POST":
        form = FormAnimal(request.POST)
                        
        if form.is_valid():
            data = form.cleaned_data
                
            fecha = data.get("fecha_creacion") 
            if not fecha:
                fecha = datetime.now()
            
            animal = Animal(nombre = data.get("nombre"), 
                            edad = data.get("edad"),
                            fecha_creacion = fecha)
            animal.save()
           
            # listado_animal = Animal.objects.all()
            # return render(request, "listado_animal.html", {"lista_animales": listado_animal})
            return redirect("listado_completo")
        else:
            return render(request, "plantilla_for.html", {"form": form}) 
        
    animal = FormAnimal()
    return render(request, "plantilla_for.html", {"form": animal})


def listado_completo(request):
    
    nombre_de_busqueda = request.GET.get("nombre")
    
    if nombre_de_busqueda:
        listado_animal = Animal.objects.filter(nombre__icontains = nombre_de_busqueda)
    else:
        listado_animal = Animal.objects.all()
    
     
    form = BusquedaAnimal()
    return render(request, "listado_animal.html", {"lista_animales": listado_animal,"form":form})