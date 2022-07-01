from django.urls import  path 
from .views import crear_animal, vista1, vista2, listado_completo

urlpatterns = [
    path("", vista1, name = "lista"),
    path("template/", vista2, name = "primhtml"),
    path("crear-animal/", crear_animal, name = "crear-animal"),
    path("listado_completo/", listado_completo, name = "listado_completo"),
    
]