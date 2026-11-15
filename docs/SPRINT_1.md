# Sprint 1 — Revisión y retrospectiva

**Proyecto:** CulturaCerca Colombia  
**Fecha:** 14 de noviembre de 2026  
**Metodología:** Scrum  
**Sprint:** 1 de 2  
**Equipo:** Anthony, Karen y Juan  
**Repositorio:** https://github.com/skyyleerr/culturacerca-django

---

## 1. Sprint Goal

Construir una primera versión funcional de CulturaCerca Colombia que permita consultar espacios culturales registrados en Colombia mediante datos abiertos oficiales, visualizar su información en una interfaz web desarrollada con Django y buscar establecimientos por municipio.

El resultado esperado del Sprint es una aplicación navegable que permita a los ciudadanos explorar espacios culturales sin consultar directamente el archivo CSV.

## 2. Historias de usuario seleccionadas

| Historia | Responsable | Funcionalidad | Prioridad |
|---|---|---|---|
| HU-01 | Anthony | Consultar espacios culturales registrados | High |
| HU-02 | Karen | Visualizar información de espacios culturales | High |
| HU-03 | Juan | Buscar espacios culturales por municipio | High |

### Distribución técnica del trabajo

**Anthony — Procesamiento de datos**

- Incorporación del conjunto de datos CSV oficial.
- Implementación del servicio de lectura y procesamiento de registros.
- Obtención de municipios disponibles.
- Desarrollo de pruebas para verificar la lectura y búsqueda de datos.

**Karen — Interfaz de usuario**

- Desarrollo de la plantilla HTML principal.
- Diseño de las tarjetas de espacios culturales.
- Implementación de estilos CSS.
- Presentación de la información y controles de navegación.
- Adaptación de la interfaz a diferentes tamaños de pantalla.

**Juan — Integración Django**

- Implementación de las vistas Django.
- Integración del servicio de datos con las plantillas HTML.
- Desarrollo de la búsqueda por municipio.
- Implementación de paginación.
- Desarrollo de pruebas de vistas.

## 3. Sprint Review

### 3.1. Funcionalidades implementadas

Durante el Sprint 1 se preparó una primera versión funcional de CulturaCerca Colombia utilizando Python, Django, HTML y CSS.

**Consulta de espacios culturales**

La aplicación utiliza un archivo CSV descargado del portal oficial datos.gov.co, correspondiente al conjunto de datos Mapa de Espacios de las Artes, las Culturas y los Saberes.

El archivo contiene 29.961 registros de espacios culturales, con información como nombre, municipio, departamento, tipo de establecimiento y dirección cuando está disponible.

**Visualización de establecimientos**

Los resultados se presentan mediante una interfaz web organizada en tarjetas que permiten identificar fácilmente los establecimientos culturales registrados.

La información se obtiene del archivo CSV y no de registros ficticios utilizados para ilustrar la aplicación.

**Búsqueda por municipio**

Se incorporó una búsqueda que permite consultar espacios culturales pertenecientes a un municipio seleccionado.

La funcionalidad contempla diferencias entre mayúsculas y minúsculas y permite efectuar nuevas consultas desde la página principal.

**Paginación**

La aplicación divide los resultados en páginas de 12 registros para facilitar la navegación y evitar mostrar simultáneamente todos los establecimientos del conjunto de datos.

**Manejo básico de casos especiales**

La versión incorpora un mensaje para búsquedas sin coincidencias y contempla la ausencia de determinados datos, evitando que estos impidan consultar el catálogo.

### 3.2. Pruebas y verificaciones

Se prepararon pruebas automatizadas del servicio CSV y de las vistas Django, además de verificaciones manuales del recorrido principal.

#### Prueba 1 — Comprobación de configuración Django

**Comando:**

`python manage.py check`

**Resultado:**

`System check identified no issues (0 silenced).`

Este resultado indica que Django no detecta problemas en las comprobaciones de configuración del proyecto.

#### Prueba 2 — Pruebas automatizadas del servicio CSV

**Comando:**

`python -m unittest core.tests.test_csv_service -v`

**Resultado:**

`Ran 10 tests`  
`OK`

Estas pruebas abarcan la lectura de registros, obtención de municipios, búsquedas exactas, normalización de mayúsculas y tildes, ausencia de coincidencias, datos incompletos y errores del archivo.

#### Prueba 3 — Pruebas automatizadas de Django

**Comando:**

`python manage.py test`

**Resultado:**

La ejecución de las 17 pruebas incluidas en los módulos de pruebas del proyecto, sin fallos ni errores, finalizando con el mensaje `OK`.

Estas pruebas incluyen 10 verificaciones del servicio de datos y 7 comprobaciones de vistas Django.

#### Prueba 4 — Ejecución del servidor

**Comando:**

`python manage.py runserver`

**Resultado:**

Inicio del servidor de desarrollo y acceso a la aplicación mediante la dirección:

http://127.0.0.1:8000/

#### Prueba 5 — Consulta de establecimientos

**Procedimiento:**

1. Abrir la página principal.
2. Consultar los espacios culturales presentados.
3. Revisar los nombres, municipios, departamentos y tipos de establecimientos.

**Resultado esperado:**

La aplicación muestra registros obtenidos del CSV oficial, organizados de forma legible.

#### Prueba 6 — Búsqueda por municipio

**Procedimiento:**

1. Seleccionar Bogotá.
2. Ejecutar la búsqueda.
3. Repetir el procedimiento con Medellín o Soacha.

**Resultado esperado:**

Los establecimientos presentados corresponden al municipio seleccionado y el sistema permite realizar nuevas consultas.

#### Prueba 7 — Paginación

**Procedimiento:**

1. Consultar un municipio con múltiples registros.
2. Avanzar a la siguiente página.
3. Regresar a la anterior.

**Resultado esperado:**

Se muestran hasta 12 registros por página y se mantiene el municipio seleccionado al cambiar de página.

#### Prueba 8 — Búsqueda sin coincidencias

**Procedimiento:**

Ejecutar una consulta sin establecimientos coincidentes.

**Resultado esperado:**

La aplicación muestra un mensaje informativo y no genera un error bloqueante.

**Estado de las verificaciones:** los resultados descritos son los esperados conforme a las pruebas y funcionalidades implementadas. La salida real de los comandos deberá conservarse como evidencia después de ejecutarlos sobre la versión integrada en `main`.

### 3.3. Integración del incremento

El equipo utilizó un repositorio compartido en GitHub y trabajó con ramas para organizar sus aportes.

Anthony desarrolló el procesamiento del CSV y las pruebas del servicio de datos.

Debido a dificultades en el github de Karen se tuvo que incorporar conjuntamente en la rama `Juan`, conservando la identificación de sus responsabilidades.

Los cambios se enviaron mediante Pull Requests hacia la rama principal. Según el seguimiento informado por el equipo, las solicitudes fueron revisadas y aceptadas.

La integración permite reunir el servicio de datos, la interfaz web y las vistas Django necesarias para ejecutar el recorrido principal de CulturaCerca Colombia.

### 3.4. Revisión de las historias de usuario

| Historia | Implementación | Criterio para aceptación definitiva |
|---|---|---|
| HU-01 | Servicio CSV y consulta de datos | Confirmar lectura de registros reales y pruebas del servicio |
| HU-02 | Plantillas HTML y CSS | Confirmar que la interfaz presenta la información correctamente |
| HU-03 | Búsqueda por municipio y paginación | Confirmar resultados correctos y pruebas de vistas |

Las tres historias cuentan con implementación correspondiente al Sprint 1. Su aceptación definitiva requiere comprobar los criterios de aceptación y la Definition of Done en la versión integrada.

### 3.5. Pendientes detectados

El Sprint 1 se concentró en la consulta y búsqueda por municipio. Quedan para el Sprint 2 las siguientes funcionalidades:

- HU-04: permitir filtrar establecimientos por tipo de espacio cultural.
- HU-05: mejorar los mensajes para búsquedas sin resultados y registros con información incompleta.
- HU-06: permitir combinar simultáneamente filtros por municipio y tipo.

También se debe completar la verificación final de las pruebas ejecutadas desde `main` y actualizar la documentación conforme al incremento entregado.

---

## 4. Sprint Retrospective

### 4.1. ¿Qué funcionó bien?

La distribución inicial de responsabilidades permitió separar el procesamiento de datos, la interfaz y la integración Django, facilitando la identificación de las tareas de cada integrante.

El uso de un CSV oficial permitió trabajar con información real sin implementar una base de datos adicional, reduciendo la complejidad técnica del proyecto.

Se consiguió construir una primera versión web que integra diferentes componentes del sistema y ofrece una consulta útil de espacios culturales.

El uso de GitHub y los Pull Requests permitió incorporar los cambios al repositorio compartido y mantener un historial del trabajo integrado.

### 4.2. ¿Qué dificultades tuvimos?

**Fallos en el github de Karen que le impedio subir su parte al repositorio**

Al distribuir los archivos entre los integrantes, fue necesario verificar la ubicación de las plantillas HTML y los archivos estáticos para que Django pudiera reconocerlos correctamente.

**Uso inicial de Git**

Se presentaron dificultades al trabajar con repositorios clonados dentro de otras carpetas del proyecto. En algunos intentos, Git indicaba que no había cambios pendientes porque los archivos modificados estaban fuera de la carpeta controlada por el repositorio.

**Integración del trabajo colaborativo**

Por dificultades técnicas y de organización, fue necesario reunir los archivos de Karen y Juan para realizar su integración desde una misma rama.

**Dependencias entre funcionalidades**

La búsqueda desarrollada con Django dependía del servicio de lectura de datos. Por eso fue necesario coordinar el orden de integración de los cambios para evitar errores por archivos faltantes.

### 4.3. ¿Qué podemos mejorar en el Sprint 2?

Para el segundo Sprint se propone mejorar la organización del trabajo mediante:

- Verificar las rutas y la estructura de carpetas antes de realizar commits.
- Mantener una copia local del repositorio actualizada desde `main`.
- Crear ramas nuevas a partir de una versión principal previamente verificada.
- Registrar cambios pequeños y descriptivos.
- Revisar las dependencias entre las funcionalidades antes de integrarlas.
- Ejecutar pruebas después de cada integración importante.
- Mantener actualizado GitHub Projects conforme avance el trabajo.

### 4.4. Acción de mejora propuesta

**Acción:** establecer un procedimiento común de verificación antes de subir e integrar cambios.

**Responsables:** Anthony, Karen y Juan.

**Procedimiento:**

1. Actualizar la copia local del repositorio.
2. Verificar que se está trabajando en la rama correcta.
3. Comprobar los archivos modificados mediante `git status`.
4. Ejecutar las pruebas relacionadas con los cambios.
5. Realizar un commit descriptivo.
6. Abrir un Pull Request y solicitar revisión.
7. Integrar el cambio y ejecutar nuevamente las verificaciones necesarias.

**Comprobación:** durante el Sprint 2, revisar que cada cambio integrado tenga una descripción clara, archivos correctamente ubicados y evidencias de verificación.

---

## 5. Conclusiones del Sprint 1

El Sprint 1 permitió desarrollar la base funcional de CulturaCerca Colombia mediante una aplicación Django que consulta espacios culturales reales, presenta su información y permite búsquedas por municipio.

La distribución de responsabilidades facilitó el desarrollo de los diferentes componentes y mostró la importancia de coordinar su integración.

Las dificultades relacionadas con Git y la organización de carpetas permitieron identificar mejoras para el siguiente Sprint, especialmente en el control de versiones y las verificaciones previas a cada Pull Request.

El incremento proporciona una base para implementar las funcionalidades restantes del Sprint 2: filtrado por tipo de establecimiento, manejo mejorado de resultados vacíos y búsqueda combinada.

## 6. Evidencias del proyecto

**Repositorio principal:**  
https://github.com/skyyleerr/culturacerca-django

**Historial de Pull Requests:**  
https://github.com/skyyleerr/culturacerca-django/pulls

En este historial se encuentran las solicitudes correspondientes al procesamiento de datos de Anthony y a la integración de interfaz y búsqueda realizada desde la rama de Juan.

**GitHub Project:**  
https://github.com/users/skyyleerr/projects/2/views/1

**Fuente oficial de datos:**  
https://www.datos.gov.co/Cultura/Mapa-de-Espacios-de-las-Artes-las-Culturas-y-los-S/p9n3-av9n

**Estado de la documentación:** informe elaborado con las funcionalidades y dificultades conocidas del Sprint 1. Los resultados de pruebas indicados como esperados deberán contrastarse con su ejecución real antes de utilizarlos como evidencia de aceptación definitiva.
