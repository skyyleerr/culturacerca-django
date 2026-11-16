"""HU-03 y HU-06 (Juan): búsqueda por municipio y tipo, con paginación."""
import logging

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render

from .services.csv_service import (
    CatalogoError,
    buscar_por_municipio,
    buscar_por_tipo,
    cargar_catalogo,
    obtener_municipios,
    obtener_tipos,
)

logger = logging.getLogger(__name__)


def home(request):
    """Consultar el CSV filtrando por municipio, tipo, ambos o ninguno."""
    municipio_seleccionado = request.GET.get("municipio", "").strip()[:160]
    tipo_seleccionado = request.GET.get("tipo", "").strip()[:160]
    contexto = {
        "municipio_seleccionado": municipio_seleccionado,
        "tipo_seleccionado": tipo_seleccionado,
        "municipios": [],
        "tipos": [],
        "total_espacios": 0,
        "total_resultados": 0,
        "page_obj": None,
        "error_catalogo": False,
        "fuente_datos": settings.CULTURAL_SPACES_SOURCE,
        "filtros_activos": bool(municipio_seleccionado or tipo_seleccionado),
    }
    try:
        espacios = cargar_catalogo(str(settings.CULTURAL_SPACES_CSV))
        # Orden importa solamente para el costo: ambos filtros son exactos y
        # pueden usarse de forma independiente o simultánea (intersección).
        por_municipio = buscar_por_municipio(espacios, municipio_seleccionado)
        resultados = buscar_por_tipo(por_municipio, tipo_seleccionado)
        paginador = Paginator(resultados, settings.RESULTS_PER_PAGE)
        pagina = paginador.get_page(request.GET.get("page", 1))
        contexto.update(
            municipios=obtener_municipios(espacios),
            tipos=obtener_tipos(espacios),
            total_espacios=len(espacios),
            total_resultados=len(resultados),
            page_obj=pagina,
        )
    except CatalogoError:
        logger.exception("No se pudo cargar el catálogo de espacios culturales")
        contexto["error_catalogo"] = True
        return render(request, "core/home.html", contexto, status=503)
    return render(request, "core/home.html", contexto)
