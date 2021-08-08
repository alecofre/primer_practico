from django.shortcuts import render,redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.
def root(request):
     return redirect("/blogs")

def index(request):
     return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
     return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
     return redirect("/")

def show(request,number):
     return HttpResponse(f"place hoder para mostrar el blog número: {number}")

def edit(request,number):
     return HttpResponse(f"placeholder para editar el blog {number}")

def destroy(request,number):
     return redirect("/blogs")

def json(request):
     return JsonResponse({"Titulo": "Placeholder para mostrar un Json",
     "Nombre": "Ale","Apellido": "Cofre","Curso": "curso 0071"})

