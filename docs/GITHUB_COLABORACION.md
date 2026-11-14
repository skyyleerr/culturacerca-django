# Integración del Sprint 1 en GitHub (sin inventar contribuciones)

**Repositorios:**
- https://github.com/skyyleerr/culturacerca-django
- https://github.com/users/skyyleerr/projects/2/views/1

**Hay dos paquetes diferentes:**
1. `CulturaCerca_Starter_Para_Main.zip`: base técnica que se sube inicialmente a `main`.
2. `CulturaCerca_Colombia_Sprint_1_Django.zip`: referencia completa del Sprint 1, cuyos archivos serán desarrollados, comprobados e integrados en las ramas de cada integrante.

Los archivos de referencia no son evidencia de autoría. Cada integrante debe trabajar realmente en su rama, verificar sus cambios y explicar su PR.

## A. Inicializar `main` con el starter — Juan

1. Si el repositorio está vacío, entra a `Code → creating a new file`, crea `README.md` y confirma el commit para crear `main`.
2. En Windows CMD, desde una carpeta de trabajo:

```cmd
git clone https://github.com/skyyleerr/culturacerca-django.git
cd culturacerca-django
```

3. Extrae **el contenido interior** de `culturacerca-django-starter` al directorio recién clonado (donde está `.git`). Revisa que `manage.py` quede en la raíz; no copies la carpeta `.git` de otros proyectos.
4. Antes de hacer commit, verifica:

```cmd
py -3.14 -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py check
python manage.py runserver
```

5. Abre `http://127.0.0.1:8000/`, verifica la página del starter y detén con `Ctrl+C`.
6. Publica la base:

```cmd
git add .
git commit -m "chore: initialize Django project starter"
git push origin main
```

## B. Anthony: HU-01 (servicio de datos)

En su PC, Anthony clona, instala y trabaja en su rama:

```cmd
git clone https://github.com/skyyleerr/culturacerca-django.git
cd culturacerca-django
git checkout -b feature/data-processing
```

Implementa/revisa los contenidos de estos archivos de la solución de referencia:
- `data/espacios_culturales.csv`
- `data/FUENTE.txt`
- `core/services/__init__.py`
- `core/services/csv_service.py`
- `core/tests/__init__.py`
- `core/tests/test_csv_service.py`

Verificación mínima sin Django: `python -m unittest core.tests.test_csv_service -v`.

```cmd
git add data core/services core/tests/test_csv_service.py
git commit -m "feat: load official cultural spaces CSV"
git push -u origin feature/data-processing
```

Luego PR con `Refs #N`, indicando el número real de HU-01. Otro integrante revisa y, si cumple la DoD, integra.

## C. Karen: HU-02 (interfaz)

Después de integrar a Anthony, Karen clona o actualiza `main` y crea una rama propia:

```cmd
git checkout main
git pull origin main
git checkout -b feature/user-interface
```

Implementa/revisa:
- `core/templates/core/base.html`
- `core/templates/core/home.html`
- `core/static/core/styles.css`

Al probar el código **antes de integrar la vista de Juan**, la plantilla final necesita las variables de contexto (`page_obj`, `municipios`, etc.). Karen puede verificar su estructura visual, pero el recorrido completo se comprueba durante la integración.

```cmd
git add core/templates core/static
git commit -m "feat: create cultural spaces catalog interface"
git push -u origin feature/user-interface
```

Abre PR que otra persona revisa y, si es apropiado, integra.

## D. Juan: HU-03 (vista + búsqueda)

Tras actualizar `main`:

```cmd
git checkout main
git pull origin main
git checkout -b feature/django-integration
```

Implementa/revisa:
- `core/views.py` (reemplaza la vista de demostración del starter)
- `core/tests/test_views.py`
- `core/urls.py` (si requiere ajustes)
- `README.md` (instrucciones definitivas)

Las configuraciones necesarias ya están previstas en el starter `config/settings.py`.

```cmd
python manage.py check
python manage.py test
python manage.py runserver
```

Comprueba `/` y `/?municipio=Bogot%C3%A1%2C+D.C.` en el navegador.

```cmd
git add core/views.py core/tests/test_views.py README.md
git commit -m "feat: integrate municipality search in Django"
git push -u origin feature/django-integration
```

Abre PR y solicita revisión. No marques la historia Done antes de verificar.

## E. Crear y revisar cada Pull Request desde GitHub

1. Abre `Pull requests` → `New pull request`.
2. Selecciona `base: main`, `compare: feature/<rama>`.
3. Título en inglés, p. ej. `feat: support municipality search`.
4. En descripción:

```markdown
## What changed
- [cambios hechos realmente]

## Why
- [valor de la historia]

## Related issue
Refs #N

## How it was verified
- [comando realmente ejecutado]
- [resultado observado]

## Reviewer
- [compañero que revisó]
```

5. Haz clic en `Create pull request`.
6. Pide revisión a otro integrante; solo acepta el PR cuando el cambio se haya comprobado.
7. Integra con `Merge pull request` y actualiza el Project según el estado real.

## Sprint 2 — todavía no implementar aquí
- HU-04, Anthony: filtrar por tipo.
- HU-05, Karen: manejo avanzado de vacíos e incompletos.
- HU-06, Juan: combinar municipio y tipo.
