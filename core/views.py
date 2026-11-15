"""HU-03 (Juan): vista Django, filtro por municipio y paginación."""
import logging

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render

from .services.csv_service import (
    CatalogoError,
    buscar_por_municipio,
    cargar_catalogo,
    obtener_municipios,
)

logger = logging.getLogger(__name__)


def home(request):
    municipio_seleccionado = request.GET.get("municipio", "").strip()[:160]
    contexto = {
        "municipio_seleccionado": municipio_seleccionado,
        "municipios": [],
        "total_espacios": 0,
        "total_resultados": 0,
        "page_obj": None,
        "error_catalogo": False,
        "fuente_datos": settings.CULTURAL_SPACES_SOURCE,
    }
    try:
        espacios = cargar_catalogo(str(settings.CULTURAL_SPACES_CSV))
        resultados = buscar_por_municipio(espacios, municipio_seleccionado)
        paginador = Paginator(resultados, settings.RESULTS_PER_PAGE)
        pagina = paginador.get_page(request.GET.get("page", 1))
        contexto.update(
            municipios=obtener_municipios(espacios),
            total_espacios=len(espacios),
            total_resultados=len(resultados),
            page_obj=pagina,
        )
    except CatalogoError:
        logger.exception("No se pudo cargar el catálogo de espacios culturales")
        contexto["error_catalogo"] = True
        return render(request, "core/home.html", contexto, status=503)
    return render(request, "core/home.html", contexto)
