from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template  import loader

def saludo(request: HttpRequest) -> HttpResponse:
        template = loader.get_template("saludo.html")
        return HttpResponse(template.render())
