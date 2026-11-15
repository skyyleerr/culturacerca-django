"""Pruebas Django de integración HU-01, HU-02 y HU-03."""
import tempfile
from pathlib import Path
from unittest.mock import patch

from django.test import SimpleTestCase, override_settings
from django.urls import reverse

from core.services.csv_service import cargar_catalogo
from core.tests.test_csv_service import DATOS_CSV


class HomeViewTests(SimpleTestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.ruta = Path(self.tempdir.name) / "catalogo.csv"
        self.ruta.write_text(DATOS_CSV, encoding="utf-8-sig")
        self.overrides = override_settings(CULTURAL_SPACES_CSV=self.ruta, RESULTS_PER_PAGE=2)
        self.overrides.enable()
        self.addCleanup(self.overrides.disable)
        cargar_catalogo.cache_clear()
        self.addCleanup(cargar_catalogo.cache_clear)

    def test_pagina_principal_muestra_datos_del_csv(self):
        respuesta = self.client.get(reverse("core:home"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Biblioteca Central")
        self.assertContains(respuesta, "Museo del Centro")
        self.assertEqual(respuesta.context["total_espacios"], 4)

    def test_buscar_por_municipio(self):
        respuesta = self.client.get("/", {"municipio": "Soacha"})
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.context["total_resultados"], 2)
        self.assertContains(respuesta, "Museo Soacha")
        self.assertNotContains(respuesta, "Biblioteca Central")

    def test_busqueda_no_distingue_mayusculas(self):
        respuesta = self.client.get("/", {"municipio": "MEDELLIN"})
        self.assertEqual(respuesta.context["total_resultados"], 1)
        self.assertContains(respuesta, "Museo del Centro")

    def test_sin_coincidencias_muestra_mensaje(self):
        respuesta = self.client.get("/", {"municipio": "Ciudad Inventada"})
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "No encontramos espacios")
        self.assertEqual(respuesta.context["total_resultados"], 0)

    def test_paginacion_preserva_filtro(self):
        respuesta = self.client.get("/", {"municipio": "Soacha", "page": 2})
        self.assertEqual(respuesta.context["page_obj"].number, 1)
        respuesta_todos = self.client.get("/", {"page": 2})
        self.assertEqual(respuesta_todos.context["page_obj"].number, 2)
        self.assertContains(respuesta_todos, "?municipio=&amp;page=1", html=False)

    def test_direccion_vacia_no_presenta_none(self):
        respuesta = self.client.get("/", {"municipio": "Medellín"})
        self.assertContains(respuesta, "Dirección no disponible")

    def test_archivo_ausente_responde_503(self):
        with override_settings(CULTURAL_SPACES_CSV=self.ruta.parent / "no-existe.csv"):
            respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 503)
        self.assertContains(respuesta, "No pudimos cargar", status_code=503)
