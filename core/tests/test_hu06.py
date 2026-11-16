"""HU-06 (Juan): pruebas Django de la búsqueda por municipio + tipo."""
import tempfile
from pathlib import Path

from django.test import SimpleTestCase, override_settings

from core.services.csv_service import cargar_catalogo
from core.tests.test_csv_service import DATOS_CSV


class BusquedaCombinadaViewTests(SimpleTestCase):
    def setUp(self):
        self.directorio = tempfile.TemporaryDirectory()
        self.addCleanup(self.directorio.cleanup)
        self.ruta = Path(self.directorio.name) / "catalogo.csv"
        self.ruta.write_text(DATOS_CSV, encoding="utf-8-sig")
        configuracion = override_settings(CULTURAL_SPACES_CSV=self.ruta, RESULTS_PER_PAGE=1)
        configuracion.enable()
        self.addCleanup(configuracion.disable)
        cargar_catalogo.cache_clear()
        self.addCleanup(cargar_catalogo.cache_clear)

    def test_buscar_municipio_y_tipo_juntos(self):
        respuesta = self.client.get("/", {"municipio": "Soacha", "tipo": "Museo"})
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.context["total_resultados"], 1)
        self.assertContains(respuesta, "Museo Soacha")
        self.assertNotContains(respuesta, "Biblioteca Sur")
        self.assertNotContains(respuesta, "Museo del Centro")

    def test_filtros_se_mantienen_en_contexto_y_formulario(self):
        respuesta = self.client.get("/", {"municipio": "Soacha", "tipo": "Museo"})
        self.assertEqual(respuesta.context["municipio_seleccionado"], "Soacha")
        self.assertEqual(respuesta.context["tipo_seleccionado"], "Museo")
        self.assertContains(respuesta, 'name="municipio"')
        self.assertContains(respuesta, 'name="tipo"')
        self.assertContains(respuesta, 'value="Museo" selected')

    def test_combinacion_sin_coincidencias_muestra_mensaje(self):
        respuesta = self.client.get("/", {"municipio": "Soacha", "tipo": "Escuela de Danza"})
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.context["total_resultados"], 0)
        self.assertContains(respuesta, "No encontramos espacios para esta combinación")

    def test_limpiar_filtros_retorna_todo_el_catalogo(self):
        respuesta = self.client.get("/", {"municipio": "Soacha", "tipo": "Museo"})
        self.assertContains(respuesta, "Limpiar filtros")
        sin_filtros = self.client.get("/")
        self.assertEqual(sin_filtros.context["total_resultados"], 4)

    def test_paginacion_conserva_ambos_filtros(self):
        with self.ruta.open("a", encoding="utf-8") as archivo:
            archivo.write("Museo,Cundinamarca,Soacha,Museo Adicional,Calle 7\n")
        cargar_catalogo.cache_clear()
        respuesta = self.client.get("/", {"municipio": "Soacha", "tipo": "Museo", "page": 1})
        self.assertEqual(respuesta.context["total_resultados"], 2)
        self.assertContains(respuesta, "?municipio=Soacha&amp;tipo=Museo&amp;page=2", html=False)
        segunda = self.client.get("/", {"municipio": "Soacha", "tipo": "Museo", "page": 2})
        self.assertEqual(segunda.context["page_obj"].number, 2)
        self.assertContains(segunda, "Museo Adicional")
