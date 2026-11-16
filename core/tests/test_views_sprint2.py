"""HU-05/HU-06: pruebas de filtros combinados y estados de interfaz."""
import tempfile
from pathlib import Path

from django.test import SimpleTestCase, override_settings

from core.services.csv_service import cargar_catalogo
from core.tests.test_csv_service import DATOS_CSV


class SearchSprint2Tests(SimpleTestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.ruta = Path(self.tempdir.name) / "cultural.csv"
        self.ruta.write_text(DATOS_CSV, encoding="utf-8-sig")
        self.override = override_settings(CULTURAL_SPACES_CSV=self.ruta, RESULTS_PER_PAGE=2)
        self.override.enable()
        self.addCleanup(self.override.disable)
        cargar_catalogo.cache_clear()
        self.addCleanup(cargar_catalogo.cache_clear)

    def test_tipos_disponibles_en_el_formulario(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn("Museo", respuesta.context["tipos"])
        self.assertContains(respuesta, 'name="tipo"')

    def test_busqueda_solo_por_tipo(self):
        respuesta = self.client.get("/", {"tipo": "Museo"})
        self.assertEqual(respuesta.context["total_resultados"], 2)
        self.assertContains(respuesta, "Museo del Centro")
        self.assertNotContains(respuesta, "Biblioteca Central")

    def test_busqueda_por_tipo_no_distingue_mayusculas(self):
        respuesta = self.client.get("/", {"tipo": "mUsEo"})
        self.assertEqual(respuesta.context["total_resultados"], 2)

    def test_busqueda_combinada_interseccion(self):
        respuesta = self.client.get("/", {"municipio": "Soacha", "tipo": "Museo"})
        self.assertEqual(respuesta.context["total_resultados"], 1)
        self.assertContains(respuesta, "Museo Soacha")
        self.assertNotContains(respuesta, "Biblioteca Sur")
        self.assertEqual(respuesta.context["municipio_seleccionado"], "Soacha")
        self.assertEqual(respuesta.context["tipo_seleccionado"], "Museo")

    def test_sin_coincidencias_con_dos_filtros(self):
        respuesta = self.client.get("/", {"municipio": "Soacha", "tipo": "Escuela de danza"})
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.context["total_resultados"], 0)
        self.assertContains(respuesta, "No encontramos espacios para esta combinación")

    def test_sin_coincidencias_solo_tipo(self):
        respuesta = self.client.get("/", {"tipo": "Planetario"})
        self.assertEqual(respuesta.context["total_resultados"], 0)
        self.assertContains(respuesta, "No encontramos espacios de ese tipo")

    def test_direccion_ausente_se_presenta_sin_valores_tecnicos(self):
        respuesta = self.client.get("/", {"municipio": "Medellín"})
        self.assertContains(respuesta, "Dirección no disponible")
        self.assertContains(respuesta, "data-missing")
        self.assertNotContains(respuesta, ">None<")
        self.assertNotContains(respuesta, ">NaN<")

    def test_paginacion_conserva_dos_filtros(self):
        # Preparar una segunda coincidencia del mismo municipio y tipo.
        with self.ruta.open("a", encoding="utf-8") as archivo:
            archivo.write("Museo,Cundinamarca,Soacha,Museo Alterno,Calle 8\n")
        cargar_catalogo.cache_clear()

        with override_settings(RESULTS_PER_PAGE=1):
            respuesta = self.client.get("/", {"municipio": "Soacha", "tipo": "Museo", "page": 1})
            self.assertEqual(respuesta.context["total_resultados"], 2)
            self.assertContains(respuesta, "?municipio=Soacha&amp;tipo=Museo&amp;page=2", html=False)
            respuesta2 = self.client.get("/", {"municipio": "Soacha", "tipo": "Museo", "page": 2})
            self.assertEqual(respuesta2.context["page_obj"].number, 2)
            self.assertContains(respuesta2, "Museo Alterno")

    def test_tipo_seleccionado_permanece_visible(self):
        respuesta = self.client.get("/", {"tipo": "Museo"})
        self.assertContains(respuesta, 'value="Museo" selected')

    def test_limpiar_filtros_restablece_consulta(self):
        respuesta = self.client.get("/", {"municipio": "Soacha", "tipo": "Museo"})
        self.assertContains(respuesta, "Limpiar filtros")
        respuesta_sin = self.client.get("/")
        self.assertEqual(respuesta_sin.context["total_resultados"], 4)
