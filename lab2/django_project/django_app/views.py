from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def saludo(request: HttpRequest) -> HttpResponse:
        estudiante = "Gabriel Serrano Rojas"
        return HttpResponse(f"Estudiante: {estudiante}. Esta es mi versión esqueleto del proyecto.")
