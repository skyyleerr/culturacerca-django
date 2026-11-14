"""HU-01/HU-02/HU-03: consultar espacios desde la ruta principal."""
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
]
