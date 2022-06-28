from django.urls import  path 
from .views import vista1, vista2, vista3

urlpatterns = [
    path("", vista1),
    path("template/", vista2),
    path("lista/", vista3)
]