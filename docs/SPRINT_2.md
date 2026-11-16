# CulturaCerca Colombia — Sprint 2

**Fecha:** domingo 15 de noviembre de 2026  
**Entrega:** antes de las 23:59 (hora de Colombia)  
**Repositorio:** https://github.com/skyyleerr/culturacerca-django  
**Project:** https://github.com/users/skyyleerr/projects/2/views/1

## Sprint Goal

Completar el catálogo cultural permitiendo filtrar por tipo de espacio, combinar municipio y tipo, y comunicar claramente búsquedas sin resultados e información ausente.

## Sprint Backlog

| Historia | Responsable principal | Tareas de implementación | Verificación |
|---|---|---|---|
| HU-04 | Anthony | `obtener_tipos`, `buscar_por_tipo`, pruebas unitarias del servicio | Tipos oficiales, filtro exacto, vacío, mayúsculas/tildes |
| HU-05 | Karen | Campo de tipo, estados vacíos, direcciones faltantes, estilos responsivos | No aparece `None`/`NaN`; mensajes claros; interfaz móvil |
| HU-06 | Juan | Conectar filtros simultáneos en `home`, preservar valores/paginación y pruebas de Django | Intersección correcta, navegación, restablecer filtros |

**Dependencias:** Anthony publica el servicio de tipos → Karen publica la interfaz → Juan conecta ambos filtros y valida el recorrido de extremo a extremo.

## Criterios de aceptación

### HU-04 — Filtro por tipo
- [ ] Los tipos ofrecidos se obtienen del CSV real, sin duplicados.
- [ ] El usuario puede filtrar por uno de esos tipos.
- [ ] Los resultados corresponden a la opción solicitada.
- [ ] Elegir todos los tipos restablece el catálogo sin filtro de tipo.

### HU-05 — Resultados vacíos y datos incompletos
- [ ] Existe un mensaje visible al no encontrar coincidencias.
- [ ] Un lugar sin dirección indica «Dirección no disponible».
- [ ] No aparecen literales técnicos como `None` o `NaN`.
- [ ] La interfaz sigue siendo legible en pantallas pequeñas.

### HU-06 — Filtros combinados
- [ ] Municipio y tipo se pueden utilizar a la vez.
- [ ] Cada resultado cumple ambas condiciones.
- [ ] Los valores elegidos permanecen visibles tras buscar.
- [ ] La paginación conserva ambos filtros.
- [ ] Se pueden limpiar todos los filtros.

## Definition of Done (aplicar a las tres historias)
- [ ] Pruebas automatizadas ejecutadas sin errores bloqueantes.
- [ ] Comprobación `python manage.py check` satisfactoria.
- [ ] Recorrido real comprobado en el navegador con el CSV oficial.
- [ ] El README permite ejecutar el proyecto desde cero.
- [ ] Cambios revisados mediante Pull Requests y fusionados en `main`.
- [ ] Se registran los resultados de pruebas y revisión.
- [ ] El Project está actualizado con los estados reales.

## Pruebas propuestas

```cmd
python manage.py check
python manage.py test
python manage.py runserver
```

Casos manuales esperados:
1. Sin filtros: catálogo nacional con paginación.
2. Municipio `Bogotá, D.C.`: solo resultados de Bogotá.
3. Tipo `Museo / Entidad Museal`: solo espacios de ese tipo, según datos reales.
4. Ambos filtros: intersección exacta sin registros ajenos.
5. Combinación sin resultados: mensaje claro y botón para restablecer.
6. Registro sin dirección: «Dirección no disponible».
7. Páginas siguientes/anteriores: conservar selecciones.

## Sprint Review — completar tras realizarla

- **Fecha y hora de revisión:** [Completar]
- **Incremento demostrado:** [Completar]
- **Comandos y resultados reales:** [Completar con salida de CMD]
- **Issues aceptados:** [Completar, según criterios y DoD]
- **Enlaces de PR:** [Pegar URLs reales]
- **Pendientes o incidencias:** [Completar]

## Retrospectiva — completar con lo que realmente ocurrió

- **Qué funcionó:** [Completar]
- **Qué dificultó el trabajo:** [Completar]
- **Acción concreta de mejora y responsable:** [Completar]

> El código y las pruebas del ZIP son materiales de implementación. No constituyen evidencia de que el equipo ya haya ejecutado pruebas, revisiones o PR.
