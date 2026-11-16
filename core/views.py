"""HU-03 y HU-06 (Juan): búsqueda por municipio y tipo, con paginación."""
import logging

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render

from .services.csv_service import (
    CatalogoError,
    cargar_catalogo,
    obtener_municipios,
    obtener_tipos,
)

from .services.busqueda_combinada import extraer_filtros, filtrar_por_municipio_y_tipo

logger = logging.getLogger(__name__)


def home(request):
    """Consultar el CSV filtrando por municipio, tipo, ambos o ninguno."""
    municipio_seleccionado, tipo_seleccionado = extraer_filtros(request.GET)
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
        # HU-06: intersección de municipio y tipo en un único módulo reutilizable.
        resultados = filtrar_por_municipio_y_tipo(
            espacios, municipio=municipio_seleccionado, tipo=tipo_seleccionado
        )
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
