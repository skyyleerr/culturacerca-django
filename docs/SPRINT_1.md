# Sprint 1 — 14 de noviembre de 2026

> Documento de planificación. No presenta como realizados commits, Pull Requests, revisiones ni pruebas todavía no ejecutadas por el equipo.

## Product Goal

Facilitar la exploración de espacios culturales registrados en Colombia, con información oficial, búsqueda por municipio e interfaz web comprensible.

## Sprint Goal

Entregar una primera versión navegable en Django que permita consultar registros culturales reales y filtrar exactamente por municipio.

## Sprint Backlog

| Historia | Responsable | Implementación prevista | Verificación |
|---|---|---|---|
| HU-01 | Anthony | `core/services/csv_service.py`, dataset CSV | Pruebas de carga, municipio único, campos ausentes |
| HU-02 | Karen | `core/templates/core/`, `core/static/core/` | Consulta visual de tarjetas y navegación |
| HU-03 | Juan | `config/`, `core/views.py`, `core/urls.py` y pruebas de integración | Búsqueda exacta, sin coincidencias, paginación |

### Dependencias
1. Juan prepara y comparte el esqueleto Django.
2. Anthony desarrolla el servicio CSV con interfaz acordada (`cargar_catalogo`, `buscar_por_municipio`, `obtener_municipios`).
3. Karen prepara plantillas que reciben `page_obj`, `municipios`, `municipio_seleccionado` y totales.
4. Juan integra, solicita revisión y conecta las vistas.
5. Se ejecutan las pruebas, se verifican los criterios de aceptación, se integran los PR y se revisa la DoD.

## Definition of Done (DoD)
- [ ] La aplicación inicia sin errores bloqueantes.
- [ ] Los datos provienen del CSV oficial y su fuente queda documentada.
- [ ] Las tres historias cumplen criterios de aceptación.
- [ ] La navegación y la búsqueda funcionan desde el navegador.
- [ ] La búsqueda sin coincidencias produce un mensaje entendible.
- [ ] Existen pruebas funcionales ejecutadas con resultados anotados.
- [ ] Cada contribución se integra mediante PR revisado por otro integrante cuando sea posible.
- [ ] El README permite ejecutar el proyecto.
- [ ] GitHub Projects indica el estado real, y solo pasa a Done después de la DoD.

## Sprint Review — completar realmente
- Fecha y hora:
- Demostración realizada:
- Casos probados:
- Resultados:
- Pendientes:

## Retrospectiva — completar realmente
- ¿Qué funcionó?
- ¿Qué obstaculizó el desarrollo?
- ¿Qué cambiará el equipo para el Sprint 2?
- Acción de mejora y responsable:
