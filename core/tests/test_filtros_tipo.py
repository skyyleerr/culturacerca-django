"""HU-04: pruebas del servicio para filtrar por tipo de espacio cultural."""
import unittest

from core.services.csv_service import EspacioCultural, buscar_por_tipo, obtener_tipos


class TypeFilterTests(unittest.TestCase):
    def setUp(self):
        self.espacios = (
            EspacioCultural("Museo A", "Bogotá, D.C.", "Bogotá", "Museo", "Calle 1"),
            EspacioCultural("Biblioteca A", "Bogotá, D.C.", "Bogotá", "Biblioteca", "Calle 2"),
            EspacioCultural("Museo B", "Medellín", "Antioquia", "Museo", "Calle 3"),
            EspacioCultural("Teatro", "Cali", "Valle", "Espacio Escénico", "Calle 4"),
        )

    def test_obtener_tipos_unicos_y_ordenados(self):
        self.assertEqual(obtener_tipos(self.espacios), ["Biblioteca", "Espacio Escénico", "Museo"])

    def test_filtrar_tipo_exacto(self):
        resultados = buscar_por_tipo(self.espacios, "Museo")
        self.assertEqual(len(resultados), 2)
        self.assertTrue(all(e.tipo == "Museo" for e in resultados))

    def test_tipo_vacio_devuelve_todos(self):
        self.assertEqual(buscar_por_tipo(self.espacios, ""), self.espacios)

    def test_tipo_inexistente_sin_coincidencias(self):
        self.assertEqual(buscar_por_tipo(self.espacios, "Planetario"), ())

    def test_ignora_mayusculas_y_tildes(self):
        resultados = buscar_por_tipo(self.espacios, "espacio escenico")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].nombre, "Teatro")

    def test_no_modifica_los_registros_originales(self):
        original = self.espacios
        buscar_por_tipo(self.espacios, "Museo")
        self.assertEqual(self.espacios, original)
