"""HU-06 (Juan): composición de filtros del catálogo cultural.

Reutiliza las funciones de Anthony (HU-01/HU-04) sin modificar el CSV ni
repetir la lógica de normalización de tildes o mayúsculas.
"""

from .csv_service import buscar_por_municipio, buscar_por_tipo

LONGITUD_MAXIMA_FILTRO = 160


def extraer_filtros(parametros):
    """Lee y limpia ambos filtros GET; una selección vacía equivale a 'todos'."""
    municipio = (parametros.get("municipio") or "").strip()[:LONGITUD_MAXIMA_FILTRO]
    tipo = (parametros.get("tipo") or "").strip()[:LONGITUD_MAXIMA_FILTRO]
    return municipio, tipo


def filtrar_por_municipio_y_tipo(espacios, municipio="", tipo=""):
    """Devuelve la intersección de ambos filtros, o todos si no hay selección.

    No modifica los registros originales. Cada función del servicio CSV realiza
    comparaciones exactas ignorando mayúsculas y tildes.
    """
    resultados_municipio = buscar_por_municipio(espacios, municipio)
    return buscar_por_tipo(resultados_municipio, tipo)
