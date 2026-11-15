# CulturaCerca Colombia

Aplicación web desarrollada con **Python y Django** para consultar espacios culturales registrados en Colombia, utilizando datos abiertos oficiales del portal datos.gov.co.

Proyecto desarrollado durante el Hackathon 2026, mediante Scrum y trabajo colaborativo con GitHub.

## 1. Integrantes

| Integrante | Responsabilidades |
|---|---|
| Anthony | Procesamiento del CSV y filtrado de datos |
| Karen | Interfaz HTML, CSS y presentación de resultados |
| Juan | Vistas Django, búsqueda, paginación e integración |

## 2. Product Goal

Facilitar a ciudadanos, estudiantes y visitantes la exploración de espacios culturales registrados en Colombia mediante una aplicación web que permita consultar información y encontrar establecimientos según su ubicación y tipo.

## 3. Fuente de datos

**Conjunto de datos:** Mapa de Espacios de las Artes, las Culturas y los Saberes.

**Portal:** Datos Abiertos de Colombia.

**URL:** https://www.datos.gov.co/Cultura/Mapa-de-Espacios-de-las-Artes-las-Culturas-y-los-S/p9n3-av9n

**Formato:** CSV descargado.

**Cantidad de registros del archivo utilizado:** 29.961.

La aplicación procesa el CSV directamente sin necesidad de utilizar MariaDB.

Algunos establecimientos tienen direcciones o descripciones incompletas.

## 4. Tecnologías

- Python 3.14.5.
- Django 6.1.3.
- HTML5 y CSS3.
- CSV.
- Git y GitHub.

## 5. Product Backlog

| Historia | Descripción | Responsable | Sprint |
|---|---|---|---|
| HU-01 | Consultar espacios culturales | Anthony | 1 |
| HU-02 | Visualizar información de establecimientos | Karen | 1 |
| HU-03 | Buscar por municipio | Juan | 1 |
| HU-04 | Filtrar establecimientos por tipo | Anthony | 2 |
| HU-05 | Mejorar resultados vacíos y datos incompletos | Karen | 2 |
| HU-06 | Combinar filtros de municipio y tipo | Juan | 2 |

Los criterios de aceptación están registrados en los Issues del repositorio.

## 6. Sprint 1 — 14 de noviembre de 2026

**Sprint Goal:** construir una primera versión funcional de CulturaCerca Colombia que permita consultar espacios culturales reales y buscarlos por municipio.

### Funcionalidades implementadas

- Lectura del CSV oficial.
- Consulta de establecimientos culturales.
- Presentación de resultados mediante tarjetas.
- Búsqueda por municipio.
- Paginación de resultados.
- Interfaz adaptable.
- Pruebas del servicio de datos y vistas Django.

### Sprint Backlog

**Historias:** HU-01, HU-02 y HU-03.

**Distribución:** Anthony implementó el procesamiento del CSV; Karen desarrolló la interfaz; Juan integró las vistas Django y la búsqueda por municipio.

**Revisión y retrospectiva:** [Consultar documentación del Sprint 1](docs/SPRINT_1.md).

## 7. Sprint 2 — 15 de noviembre de 2026

**Sprint Goal:** completar la búsqueda mediante filtros por tipo de establecimiento, combinación de filtros y manejo mejorado de información incompleta.

### Historias planificadas

- HU-04: filtrar por tipo de espacio cultural.
- HU-05: mejorar mensajes para resultados vacíos y datos incompletos.
- HU-06: combinar filtros por municipio y tipo.

Estas funcionalidades forman parte del alcance planificado para el Sprint 2.

## 8. Instalación del proyecto

### Requisitos previos

- Python 3.14.
- Git.
- Conexión a internet para instalar las dependencias.

### Clonar el repositorio

```bat
git clone https://github.com/skyyleerr/culturacerca-django.git
cd culturacerca-django
```

### Crear y activar el entorno virtual

```bat
py -3.14 -m venv .venv
.venv\Scripts\activate
```

### Instalar dependencias

```bat
python -m pip install -r requirements.txt
```

### Comprobar la configuración

```bat
python manage.py check
```

### Ejecutar las pruebas

```bat
python manage.py test
```

### Iniciar el servidor

```bat
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## 9. Pruebas y verificaciones

Se incluyen pruebas automatizadas para el procesamiento del CSV y las vistas Django.

Los comandos de comprobación son:

```bat
python manage.py check
python manage.py test
```

Los resultados reales de las verificaciones deben registrarse en la documentación de cada Sprint.

## 10. Definition of Done

Para aceptar una historia de usuario se requiere:

- Cumplir los criterios de aceptación definidos.
- Utilizar datos reales correctamente.
- Verificar que la funcionalidad no presente errores bloqueantes.
- Ejecutar las pruebas correspondientes.
- Registrar los cambios en Git.
- Revisar e integrar el Pull Request.
- Mantener actualizada la documentación.
- Confirmar el funcionamiento del incremento integrado.

## 11. Scrum y GitHub

**Repositorio:**  
https://github.com/skyyleerr/culturacerca-django

**GitHub Project:**  
https://github.com/users/skyyleerr/projects/2/views/1

**Issues:**  
https://github.com/skyyleerr/culturacerca-django/issues

**Pull Requests:**  
https://github.com/skyyleerr/culturacerca-django/pulls

El trabajo se organiza mediante los estados Backlog, Ready, In Progress, In Review y Done, con prioridades High, Medium y Low.

## 12. Estado del proyecto

- **Sprint 1:** funcionalidades desarrolladas e integradas.
- **Sprint 2:** funcionalidades planificadas para el siguiente incremento.
- **Entrega final:** 15 de noviembre de 2026, antes de las 23:59.
