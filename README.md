# CulturaCerca Colombia

**Hackathon: Innovación con Datos Abiertos de Colombia**  
*Lema: Construye, aprende e innova.*

Aplicación web desarrollada en **Python y Django** para descubrir y consultar espacios culturales registrados en Colombia a partir de datos abiertos oficiales. Permite buscar por municipio, filtrar por tipo de establecimiento, combinar ambos criterios y navegar por los resultados.

**Repositorio:** https://github.com/skyyleerr/culturacerca-django  
**GitHub Project:** https://github.com/users/skyyleerr/projects/2/views/1  
**Equipo:** Anthony, Karen y Juan  
**Jornadas de trabajo:** 14 y 15 de noviembre de 2026

---

## 1. Descubrimiento del problema y propuesta de valor

### Hipótesis de necesidad

La información sobre espacios culturales de Colombia existe en conjuntos de datos públicos, pero consultar directamente un archivo con miles de filas puede resultar poco práctico para una persona que solo desea encontrar establecimientos de su municipio o de una categoría cultural específica.

**Hipótesis:** ciudadanos, estudiantes y visitantes podrían beneficiarse de una aplicación sencilla que organice esos registros y permita búsquedas útiles. Esta necesidad se plantea como **hipótesis de trabajo**, no como un problema validado mediante entrevistas a usuarios.

### Beneficiarios potenciales

- Ciudadanos que desean conocer espacios culturales de su municipio.
- Estudiantes que realizan consultas sobre infraestructura cultural.
- Visitantes interesados en bibliotecas, museos u otros tipos de establecimientos.

### Pregunta orientadora

**¿Qué espacios culturales están registrados en un municipio colombiano y a qué tipo pertenecen?**

### Solución desarrollada

Un catálogo web que consulta el conjunto de datos descargado, permite encontrar registros por **municipio**, **tipo de espacio** o **ambos filtros**, y muestra sus datos principales sin exigir al usuario abrir directamente el CSV.

## 2. Fuente, comprensión y limitaciones de los datos

- **Portal:** [Datos Abiertos de Colombia](https://www.datos.gov.co/).
- **Conjunto:** [Mapa de Espacios de las Artes, las Culturas y los Saberes](https://www.datos.gov.co/Cultura/Mapa-de-Espacios-de-las-Artes-las-Culturas-y-los-S/p9n3-av9n).
- **Identificador del conjunto:** `p9n3-av9n`.
- **Modalidad:** archivo descargado (CSV), sin conexión obligatoria a una API durante la consulta.
- **Fecha del archivo utilizado:** 13 de noviembre de 2026.
- **Archivo del repositorio:** `data/espacios_culturales.csv`.
- **Alcance:** archivo completo utilizado por el equipo, no una muestra reducida.
- **Registros del CSV:** **29.961**.
- **Clasificación:** **19 tipos de lugar** y **1.032 nombres de municipios distintos** en el archivo analizado; este último número no equivale necesariamente al conteo oficial de municipios únicos.

### Variables utilizadas

| Columna original | Uso en la aplicación |
|---|---|
| `Nombre_del_lugar` | Nombre del establecimiento cultural |
| `Municipio` | Búsqueda por municipio |
| `Departamento` | Contexto de ubicación |
| `Tipo_de_lugar` | Filtro por categoría cultural |
| `Dirección` | Dirección cuando está disponible |

El archivo original también contiene otros campos, como descripción, coordenadas y fuente de información; la versión entregada utiliza principalmente los indicados en la tabla.

### Calidad, límites y uso responsable

- Algunos registros carecen de dirección o descripción. La aplicación representa las direcciones vacías como **«Dirección no disponible»**.
- El catálogo refleja la información del archivo descargado; **no garantiza** que un establecimiento siga abierto, que sus horarios estén actualizados o que exista disponibilidad de actividades.
- La aplicación no inventa establecimientos para completar resultados.
- No requiere publicar contraseñas, claves ni datos personales de acceso.
- Los resultados provienen del CSV oficial y no de ejemplos ilustrativos.

## 3. Product Goal

**Facilitar a ciudadanos, estudiantes y visitantes la exploración de espacios culturales registrados en Colombia mediante una aplicación web clara que permita consultar establecimientos según municipio y tipo de espacio, aprovechando datos abiertos oficiales.**

Este objetivo describe el beneficio esperado para las personas usuarias, no una tarea técnica específica.

## 4. Funcionalidades implementadas

1. **Consulta del catálogo:** lectura de los registros culturales reales desde el CSV.
2. **Visualización web:** tarjetas con nombre, tipo, municipio, departamento y dirección disponible.
3. **Búsqueda por municipio:** comparación sin distinguir mayúsculas ni tildes.
4. **Filtro por tipo:** opciones obtenidas de los tipos realmente presentes en el archivo.
5. **Búsqueda combinada:** intersección de municipio y tipo, sin mezclar registros que no cumplan ambas condiciones.
6. **Manejo de resultados vacíos y datos incompletos:** mensajes comprensibles y valores alternativos para información ausente.
7. **Paginación:** hasta **12 registros por página**, conservando los filtros seleccionados.
8. **Restablecimiento de búsqueda:** opción para limpiar filtros y consultar nuevamente el catálogo.
9. **Manejo de fallos de lectura:** respuesta controlada cuando no se puede abrir el archivo CSV.

No se implementaron autenticación, registro de usuarios, CRUD, API REST propia ni despliegue en la nube, ya que están fuera del alcance mínimo del reto.

## 5. Tecnologías y arquitectura

- **Python:** 3.14.x (versión utilizada por el equipo).
- **Django:** `6.1.3`, fijado en `requirements.txt`.
- **Interfaz:** HTML5, CSS3 y plantillas Django.
- **Datos:** CSV leído mediante la biblioteca estándar `csv` de Python.
- **Control de versiones:** Git, GitHub, Issues, Projects y Pull Requests.

Se optó por **no utilizar MariaDB para este catálogo**. Django procesa directamente el archivo local, modalidad permitida por el reto. Aunque Django conserva una configuración predeterminada de SQLite, ninguna funcionalidad del catálogo necesita modelos persistentes ni migraciones.

### Organización de archivos principales

```text
culturacerca-django/
├── config/
│   ├── settings.py
│   └── urls.py
├── core/
│   ├── urls.py
│   ├── views.py
│   ├── services/
│   │   ├── csv_service.py
│   │   └── busqueda_combinada.py
│   ├── templates/core/
│   │   ├── base.html
│   │   └── home.html
│   ├── static/core/
│   │   └── styles.css
│   └── tests/
│       ├── test_csv_service.py
│       ├── test_views.py
│       ├── test_filtros_tipo.py
│       ├── test_views_sprint2.py
│       ├── test_busqueda_combinada.py
│       └── test_hu06.py
├── data/
│   ├── espacios_culturales.csv
│   └── FUENTE.txt
├── docs/
│   ├── SPRINT_1.md
│   └── SPRINT_2.md
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

**Responsabilidades técnicas:** `urls.py` define las rutas; `views.py` procesa las solicitudes HTTP; `services/` carga, normaliza y filtra datos; `templates/` y `static/` presentan la información; `tests/` verifica el comportamiento.

## 6. Instalación y ejecución desde cero (Windows CMD)

### Requisitos

- Python **3.14** instalado y disponible mediante el comando `py -3.14`.
- Git instalado.
- Conexión a internet **solo para clonar e instalar dependencias**; el CSV queda incluido en el repositorio.

### 6.1. Descargar el proyecto

```bat
git clone https://github.com/skyyleerr/culturacerca-django.git
cd culturacerca-django
git switch main
```

### 6.2. Crear y activar el entorno virtual

```bat
py -3.14 -m venv .venv
.venv\Scripts\activate
```

### 6.3. Instalar dependencias

```bat
python -m pip install -r requirements.txt
```

### 6.4. Verificar configuración y pruebas

```bat
python manage.py check
python manage.py test
```

### 6.5. Iniciar la aplicación

```bat
python manage.py runserver
```

Abrir en el navegador: **http://127.0.0.1:8000/**.

Para detener el servidor, utilizar `Ctrl + C` (o `Ctrl + Break` según la consola). No se necesita crear una base de datos MariaDB ni ejecutar migraciones para consultar este catálogo.

## 7. Guía rápida de uso y demostración

1. Abrir la página principal y comprobar que se presenta el catálogo cultural.
2. Escribir o seleccionar un **municipio**, por ejemplo `Bogotá, D.C.`, y presionar **Buscar espacios**.
3. Seleccionar un **tipo de espacio**, por ejemplo `Museo / Entidad Museal`, para limitar los resultados a esa categoría.
4. Aplicar **municipio y tipo simultáneamente** y comprobar que todos los resultados cumplen ambas condiciones.
5. Navegar a otra página de resultados y comprobar que se conservan las selecciones.
6. Probar una combinación sin coincidencias y observar el mensaje correspondiente.
7. Pulsar **Limpiar filtros** para volver al catálogo general.
8. Observar un registro con información ausente y confirmar que no muestra literales técnicos como `None` o `NaN`.

En una demostración se debe explicar el problema como **hipótesis**, citar la fuente del CSV y distinguir los resultados reales de los datos ficticios utilizados únicamente en pruebas automatizadas.

## 8. Planificación Scrum adaptada al hackathon

La actividad es una **simulación didáctica inspirada en Scrum**, organizada por el equipo en dos Sprints diarios. Las historias se registran en GitHub Issues y se gestionan en GitHub Projects.

### 8.1. Product Backlog priorizado

Se desglosaron seis historias pequeñas (dos por integrante) para organizar el trabajo de ambas jornadas. La actividad recomienda de dos a cuatro PBIs, pero permite adaptar la planificación al alcance real.

| Orden | Historia | Valor para el usuario | Responsable principal | Prioridad | Sprint |
|---|---|---|---|---|---|
| 1 | [HU-01](https://github.com/skyyleerr/culturacerca-django/issues/2) | Consultar espacios culturales reales | Anthony | High | 1 |
| 2 | [HU-02](https://github.com/skyyleerr/culturacerca-django/issues/3) | Visualizar información comprensible | Karen | High | 1 |
| 3 | [HU-03](https://github.com/skyyleerr/culturacerca-django/issues/4) | Buscar espacios por municipio | Juan | High | 1 |
| 4 | [HU-04](https://github.com/skyyleerr/culturacerca-django/issues/5) | Filtrar espacios por tipo | Anthony | Medium | 2 |
| 5 | [HU-05](https://github.com/skyyleerr/culturacerca-django/issues/6) | Comprender resultados vacíos y datos faltantes | Karen | Medium | 2 |
| 6 | [HU-06](https://github.com/skyyleerr/culturacerca-django/issues/7) | Combinar municipio y tipo | Juan | Medium | 2 |

Los criterios de aceptación comprobables están desarrollados en los Issues. El orden expresa la secuencia de valor y dependencias; las prioridades no son una medición de esfuerzo.

### 8.2. Sprint 1 — Sábado 14 de noviembre de 2026

**Sprint Goal:** construir una primera versión navegable que consulte espacios culturales oficiales y permita encontrarlos por municipio.

**PBIs elegidos:** HU-01, HU-02 y HU-03.

**Sprint Backlog (plan de implementación):**

| Responsable | Trabajo | Dependencia | Verificación |
|---|---|---|---|
| Anthony | Integrar CSV y servicio de lectura/consulta | Archivo oficial descargado | Registros y municipios obtenidos correctamente |
| Karen | Implementar plantillas, tarjetas y estilos | Estructura Django común | Resultados legibles en navegador |
| Juan | Conectar vistas, búsqueda y paginación | Servicio CSV y plantillas | Búsqueda exacta y navegación funcional |

**Incremento obtenido:** consulta general, visualización web y búsqueda por municipio con paginación. La revisión y retrospectiva se documentan en [docs/SPRINT_1.md](docs/SPRINT_1.md).

### 8.3. Sprint 2 — Domingo 15 de noviembre de 2026

**Sprint Goal:** completar el recorrido de consulta con filtros por tipo, combinación de criterios y tratamiento claro de datos faltantes o búsquedas sin coincidencias.

**PBIs elegidos:** HU-04, HU-05 y HU-06.

**Sprint Backlog (plan de implementación):**

| Responsable | Trabajo | Dependencia | Verificación |
|---|---|---|---|
| Anthony | Agregar obtención de tipos y filtro por categoría | Servicio CSV del Sprint 1 | Tipos reales y filtrado correcto |
| Karen | Mejorar controles, estados vacíos y visualización de ausencias | Plantillas del Sprint 1 | Mensajes legibles y diseño adaptable |
| Juan | Integrar ambos filtros, conservarlos en paginación y ampliar las pruebas | Filtros de Anthony y controles de Karen | Intersección correcta, reinicio y navegación |

**Incremento obtenido:** filtros individuales y combinados, restablecimiento de filtros y tratamiento de resultados sin coincidencias. La planificación y espacios de Review/Retrospective constan en [docs/SPRINT_2.md](docs/SPRINT_2.md); sus resultados deben reflejar lo que efectivamente verificó el equipo.

### 8.4. Definition of Done (DoD)

Una historia se considera **Done** cuando se ha comprobado que:

- Cumple sus criterios de aceptación y entrega una acción útil.
- Usa correctamente los registros reales del conjunto oficial.
- Django inicia sin errores bloqueantes.
- Las búsquedas sin coincidencias o los datos faltantes se manejan sin fallos bloqueantes.
- Se han ejecutado y registrado las verificaciones pertinentes.
- Los cambios se han revisado e integrado mediante Pull Request en `main`.
- El README y la documentación necesaria permiten reproducir el incremento.
- GitHub Issues y Projects muestran el estado real, sin dar por terminada una historia solo por fusionar su PR.

### 8.5. Seguimiento del trabajo y colaboración

- **[GitHub Project](https://github.com/users/skyyleerr/projects/2/views/1):** tablero con `Backlog`, `Ready`, `In Progress`, `In Review` y `Done`, y prioridades `High`, `Medium` y `Low`.
- **[Issues](https://github.com/skyyleerr/culturacerca-django/issues):** historias, responsables y criterios de aceptación.
- **[Pull Requests](https://github.com/skyyleerr/culturacerca-django/pulls):** cambios propuestos, revisión e integración.
- **[PR #9](https://github.com/skyyleerr/culturacerca-django/pull/9):** trabajo de filtrado por tipo y pruebas.
- **[PR #10](https://github.com/skyyleerr/culturacerca-django/pull/10):** interfaz y búsqueda combinada del Sprint 2.

Durante el trabajo surgieron conflictos de integración en `core/views.py` y dificultades con las carpetas y ramas locales. Se resolvieron conservando los componentes necesarios y comprobando el incremento conjunto. Los archivos fusionados en una misma rama no reemplazan la responsabilidad de comprender y verificar los aportes de cada integrante.

## 9. Verificación final: resultados reales

**Entorno comprobado:** Windows, entorno virtual `.venv`, Python 3.14 y Django 6.1.3.  
**Fecha de ejecución comunicada por el equipo:** 15 de noviembre de 2026.  
**Alcance:** copia local clonada del repositorio y pruebas ejecutadas desde su carpeta principal.

### Instalación

```text
Successfully installed Django-6.1.3 asgiref-3.13.0 sqlparse-0.6.1 tzdata-2026.6
```

### Comprobación de Django

**Comando:** `python manage.py check`

```text
System check identified no issues (0 silenced).
```

### Pruebas automatizadas

**Comando:** `python manage.py test`

```text
Found 46 test(s).
System check identified no issues (0 silenced).
----------------------------------------------------------------------
Ran 46 tests in 1.895s

OK
```

**Resultado: 46 pruebas ejecutadas y aprobadas, sin fallos ni errores al finalizar.**

Durante una de las pruebas apareció en el registro una excepción vinculada con un archivo temporal llamado `no-existe.csv`. Esta es una **verificación deliberada del comportamiento cuando el CSV no está disponible**; no representa un fallo de la prueba, que finalizó junto con las demás en `OK`.

### Ejecución del servidor

**Comando:** `python manage.py runserver`

```text
System check identified no issues (0 silenced).
Django version 6.1.3, using settings 'config.settings'
Starting WSGI development server at http://127.0.0.1:8000/
```

El equipo confirmó la apertura de la aplicación y el funcionamiento general del recorrido principal desde el navegador. Estos resultados respaldan la revisión del incremento; la aceptación de cada Issue debe reflejar, además, sus propios criterios de aceptación y el estado del tablero.

## 10. Sprint Review, retrospectiva y aprendizaje

### Revisión del producto

La demostración del incremento debe presentar:

1. La hipótesis de necesidad y los beneficiarios potenciales.
2. El CSV oficial utilizado y sus limitaciones.
3. Los objetivos y las funcionalidades de ambos Sprints.
4. Una búsqueda completa desde el navegador, con filtros y paginación.
5. Los **46 tests** aprobados y las condiciones de la DoD.
6. Las limitaciones que permanecen fuera del alcance, como la actualización en tiempo real de establecimientos.

### Reflexión del proceso

**Aspectos que funcionaron:** división del desarrollo en datos, interfaz e integración; uso de un CSV oficial sin dependencias de base de datos; verificaciones con Django y colaboración mediante Pull Requests.

**Obstáculos observados:** ubicaciones incorrectas de carpetas al preparar repositorios, diferencias entre ramas locales y remotas, conflictos en `core/views.py` y corrección de un archivo de pruebas con error de sintaxis.

**Mejora propuesta:** comprobar `git status`, la rama activa, los archivos modificados y las pruebas antes de cada commit y PR; integrar cambios dependientes en un orden claro y volver a ejecutar los tests tras cada fusión.

Los acuerdos definitivos de retrospectiva y su seguimiento deben documentarse según lo realmente conversado por el equipo en [docs/SPRINT_1.md](docs/SPRINT_1.md) y [docs/SPRINT_2.md](docs/SPRINT_2.md).

## 11. Estado final y alcance

**Producto implementado y verificado localmente:** catálogo Django con datos oficiales, interfaz web, búsqueda por municipio, filtrado por tipo, búsqueda combinada, tratamiento de datos faltantes y paginación. La comprobación final comunicada por el equipo terminó con **46/46 pruebas aprobadas**.

**Seguimiento administrativo:** antes de realizar la entrega, revisar que los Issues y los estados `Done` de GitHub Projects coincidan con los criterios de aceptación, las verificaciones y los Pull Requests integrados. También deben completarse los apartados pendientes de revisión y retrospectiva del Sprint 2, si todavía aparecen como plantilla.

**Entrega del equipo:** repositorio público, código reproducible, dataset atribuido, documentación Scrum y evidencias de colaboración disponibles en los enlaces anteriores.

---

**CulturaCerca Colombia — Construye, aprende e innova.**
