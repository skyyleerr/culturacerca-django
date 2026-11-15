"""Pruebas del servicio CSV (se pueden ejecutar sin instalar Django)."""
import tempfile
import unittest
from pathlib import Path

from core.services.csv_service import (
    CatalogoError,
    buscar_por_municipio,
    cargar_catalogo,
    limpiar_texto,
    obtener_municipios,
)


DATOS_CSV = """Tipo_de_lugar,Departamento,Municipio,Nombre_del_lugar,Dirección
Biblioteca,Bogotá D.C.,"Bogotá, D.C.",Biblioteca Central,Calle 1
Museo,Antioquia,Medellín,Museo del Centro,
Museo,Cundinamarca,Soacha,Museo Soacha,Calle 2
Biblioteca,Cundinamarca,Soacha,Biblioteca Sur,Calle 3
"""


class CsvServiceTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.ruta = Path(self.tempdir.name) / "catalogo.csv"
        self.ruta.write_text(DATOS_CSV, encoding="utf-8-sig")
        cargar_catalogo.cache_clear()

    def tearDown(self):
        cargar_catalogo.cache_clear()

    def test_carga_registros_reales_de_csv(self):
        espacios = cargar_catalogo(str(self.ruta))
        self.assertEqual(len(espacios), 4)
        self.assertEqual(espacios[0].nombre, "Biblioteca Central")

    def test_municipios_unicos(self):
        municipios = obtener_municipios(cargar_catalogo(str(self.ruta)))
        self.assertEqual(len(municipios), 3)
        self.assertIn("Soacha", municipios)

    def test_busqueda_exacta_por_municipio(self):
        espacios = cargar_catalogo(str(self.ruta))
        resultados = buscar_por_municipio(espacios, "Soacha")
        self.assertEqual(len(resultados), 2)
        self.assertTrue(all(e.municipio == "Soacha" for e in resultados))

    def test_ignora_mayusculas_y_tildes(self):
        espacios = cargar_catalogo(str(self.ruta))
        resultados = buscar_por_municipio(espacios, "MEDELLIN")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].municipio, "Medellín")

    def test_busqueda_vacia_retorna_todos(self):
        espacios = cargar_catalogo(str(self.ruta))
        self.assertEqual(len(buscar_por_municipio(espacios, "  ")), 4)

    def test_sin_coincidencias_retorna_tupla_vacia(self):
        espacios = cargar_catalogo(str(self.ruta))
        self.assertEqual(buscar_por_municipio(espacios, "No Existe"), ())

    def test_direccion_faltante(self):
        espacios = cargar_catalogo(str(self.ruta))
        self.assertEqual(espacios[1].direccion, "Dirección no disponible")
        self.assertEqual(limpiar_texto(None), "No disponible")

    def test_archivo_inexistente(self):
        with self.assertRaises(CatalogoError):
            cargar_catalogo(str(self.ruta.parent / "inexistente.csv"))

    def test_columnas_incorrectas(self):
        self.ruta.write_text("nombre,ciudad\nCentro,Bogotá\n", encoding="utf-8")
        cargar_catalogo.cache_clear()
        with self.assertRaises(CatalogoError):
            cargar_catalogo(str(self.ruta))


class DatasetOficialTests(unittest.TestCase):
    def test_csv_incluido_contiene_datos_reales(self):
        ruta = Path(__file__).resolve().parents[2] / "data" / "espacios_culturales.csv"
        self.assertTrue(ruta.is_file(), "El CSV oficial debe estar incluido en data/")
        registros = cargar_catalogo(str(ruta))
        self.assertEqual(len(registros), 29961)
        bogota = buscar_por_municipio(registros, "Bogotá, D.C.")
        self.assertGreater(len(bogota), 0)


if __name__ == "__main__":
    unittest.main()
