"""HU-06 (Juan): pruebas sin Django para la lógica de filtros combinados."""
import unittest

from core.services.csv_service import EspacioCultural
from core.services.busqueda_combinada import (
    extraer_filtros,
    filtrar_por_municipio_y_tipo,
)


class FiltrosCombinadosUnitTests(unittest.TestCase):
    def setUp(self):
        self.espacios = (
            EspacioCultural("Museo Soacha", "Soacha", "Cundinamarca", "Museo", "Calle 1"),
            EspacioCultural("Biblioteca Soacha", "Soacha", "Cundinamarca", "Biblioteca", "Calle 2"),
            EspacioCultural("Museo Medellín", "Medellín", "Antioquia", "Museo", "Calle 3"),
            EspacioCultural("Biblioteca Bogotá", "Bogotá, D.C.", "Bogotá", "Biblioteca", "Calle 4"),
        )

    def test_dos_filtros_devuelven_solo_la_interseccion(self):
        resultado = filtrar_por_municipio_y_tipo(self.espacios, "Soacha", "Museo")
        self.assertEqual([espacio.nombre for espacio in resultado], ["Museo Soacha"])

    def test_solamente_municipio(self):
        resultado = filtrar_por_municipio_y_tipo(self.espacios, municipio="Soacha")
        self.assertEqual(len(resultado), 2)

    def test_solamente_tipo(self):
        resultado = filtrar_por_municipio_y_tipo(self.espacios, tipo="Museo")
        self.assertEqual(len(resultado), 2)

    def test_sin_filtros_devuelve_todo(self):
        self.assertEqual(filtrar_por_municipio_y_tipo(self.espacios), self.espacios)

    def test_sin_coincidencias_devuelve_vacio(self):
        self.assertEqual(filtrar_por_municipio_y_tipo(self.espacios, "Soacha", "Teatro"), ())

    def test_comparacion_ignora_mayusculas_y_tildes(self):
        resultado = filtrar_por_municipio_y_tipo(self.espacios, "MEDELLIN", "mUsEo")
        self.assertEqual([espacio.nombre for espacio in resultado], ["Museo Medellín"])

    def test_no_modifica_registros_originales(self):
        antes = tuple(self.espacios)
        filtrar_por_municipio_y_tipo(self.espacios, "Soacha", "Museo")
        self.assertEqual(self.espacios, antes)

    def test_extraer_filtros_limpia_espacios_y_limita_longitud(self):
        municipio, tipo = extraer_filtros({"municipio": "  Soacha  ", "tipo": " Museo "})
        self.assertEqual((municipio, tipo), ("Soacha", "Museo"))
        municipio, tipo = extraer_filtros({"municipio": "x" * 300, "tipo": None})
        self.assertEqual(len(municipio), 160)
        self.assertEqual(tipo, "")
