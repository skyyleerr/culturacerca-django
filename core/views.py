"""Vista mínima del starter compartido, sin lógica del reto."""
from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")
