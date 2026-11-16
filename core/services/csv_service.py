"""HU-01 (Anthony): lectura de CSV y búsqueda exacta por municipio.

Sin ORM ni dependencias externas. El dataset permanece intacto en disco.
La cache evita leer cerca de treinta mil registros en cada solicitud.
"""
import csv
import unicodedata
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


class CatalogoError(Exception):
    """No fue posible leer el conjunto oficial de datos."""


@dataclass(frozen=True, slots=True)
class EspacioCultural:
    nombre: str
    municipio: str
    departamento: str
    tipo: str
    direccion: str


COLUMNAS_OBLIGATORIAS = {
    "Nombre_del_lugar", "Municipio", "Departamento", "Tipo_de_lugar"
}


def limpiar_texto(valor, *, alternativa="No disponible"):
    """Convierte celdas nulas o vacías a un texto legible."""
    if valor is None:
        return alternativa
    texto = str(valor).strip()
    if not texto or texto.casefold() in {"nan", "none", "null"}:
        return alternativa
    return texto


def normalizar_busqueda(texto):
    """Ignora diferencias de mayúsculas y tildes para comparar nombres."""
    texto = unicodedata.normalize("NFKD", (texto or "").strip().casefold())
    return "".join(caracter for caracter in texto if not unicodedata.combining(caracter))


@lru_cache(maxsize=4)
def cargar_catalogo(ruta_csv):
    """Devuelve una tupla inmutable de espacios culturales del CSV."""
    ruta = Path(ruta_csv)
    try:
        with ruta.open("r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)
            columnas = set(lector.fieldnames or ())
            if not COLUMNAS_OBLIGATORIAS.issubset(columnas):
                faltantes = ", ".join(sorted(COLUMNAS_OBLIGATORIAS - columnas))
                raise CatalogoError(f"El CSV no contiene las columnas esperadas: {faltantes}")
            espacios = []
            for fila in lector:
                nombre = limpiar_texto(fila.get("Nombre_del_lugar"), alternativa="")
                if not nombre:
                    continue
                espacios.append(
                    EspacioCultural(
                        nombre=nombre,
                        municipio=limpiar_texto(fila.get("Municipio")),
                        departamento=limpiar_texto(fila.get("Departamento")),
                        tipo=limpiar_texto(fila.get("Tipo_de_lugar"), alternativa="Sin clasificar"),
                        direccion=limpiar_texto(
                            fila.get("Dirección"), alternativa="Dirección no disponible"
                        ),
                    )
                )
    except (OSError, UnicodeError, csv.Error) as exc:
        raise CatalogoError("No se pudo abrir o interpretar el CSV oficial") from exc
    return tuple(espacios)


def obtener_municipios(espacios):
    """Municipios únicos, ordenados de forma predecible."""
    nombres = {e.municipio for e in espacios if e.municipio != "No disponible"}
    return sorted(nombres, key=normalizar_busqueda)


def buscar_por_municipio(espacios, municipio):
    """Filtrado exacto, sin mezclar municipios con nombres parcialmente iguales."""
    termino = normalizar_busqueda(municipio)
    if not termino:
        return espacios
    return tuple(e for e in espacios if normalizar_busqueda(e.municipio) == termino)


# -----------------------------------------------------------------------------
# Sprint 2 · HU-04 (Anthony): opciones y búsqueda exacta por tipo cultural.
# -----------------------------------------------------------------------------

def obtener_tipos(espacios):
    """Tipos del CSV, sin duplicados y ordenados ignorando tildes/caja."""
    tipos = {espacio.tipo for espacio in espacios if espacio.tipo != "Sin clasificar"}
    return sorted(tipos, key=normalizar_busqueda)


def buscar_por_tipo(espacios, tipo):
    """Devuelve todos los espacios si no se elige tipo; si no, coincidencia exacta."""
    termino = normalizar_busqueda(tipo)
    if not termino:
        return tuple(espacios)
    return tuple(
        espacio for espacio in espacios
        if normalizar_busqueda(espacio.tipo) == termino
    )
