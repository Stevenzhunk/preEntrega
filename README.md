# 🧪 Proyecto Final - QA Automation | SauceDemo

Proyecto de **QA Automation** desarrollado para automatizar pruebas funcionales sobre la aplicación web [SauceDemo](https://www.saucedemo.com/).

El proyecto utiliza **Python, Pytest, Selenium WebDriver y Behave** para validar funcionalidades de la aplicación mediante pruebas automatizadas de interfaz gráfica (UI), aplicando buenas prácticas de organización, reutilización de código y diseño de escenarios BDD.

También incorpora integración continua mediante **GitHub Actions**, permitiendo ejecutar las pruebas automáticamente ante cambios en el repositorio.

---

## 🎯 Propósito del proyecto

El objetivo es automatizar diferentes escenarios funcionales de SauceDemo, verificando el comportamiento de sus principales funcionalidades y aplicando herramientas utilizadas en procesos de aseguramiento de calidad de software.

Las pruebas se organizan en los siguientes módulos:

### 🔐 Automatización de Login

Se verifica:

- Acceso a la página de SauceDemo.
- Ingreso de usuario y contraseña.
- Inicio de sesión exitoso.
- Redirección correcta al inventario.
- Validación de credenciales incorrectas.
- Validación de usuarios bloqueados.
- Validación de campos vacíos.

### 📋 Navegación y verificación del catálogo

Se verifica:

- Título de la aplicación.
- Menú hamburguesa.
- Filtros del catálogo.
- Existencia de productos disponibles.

### 🛒 Interacción con productos y carrito

Se verifica:

- Identificación de productos del catálogo.
- Obtención de nombres y precios.
- Agregado de productos al carrito.
- Actualización del contador del carrito.
- Navegación hacia el carrito.
- Existencia de los productos agregados.
- Comparación entre los productos seleccionados y los mostrados en el carrito.

### 🌐 Automatización de pruebas API

Se implementan pruebas automatizadas sobre la API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/), utilizando la librería Requests.

Se verifican los siguientes escenarios:

- Consulta de publicaciones mediante solicitudes GET.
- Creación de publicaciones mediante solicitudes POST.
- Eliminación de publicaciones mediante solicitudes DELETE.
- Consulta de publicaciones inexistentes.
- Validación de códigos de estado HTTP.
- Verificación de los datos devueltos en las respuestas JSON.

### 🥒 Pruebas BDD con Behave

Se implementan escenarios utilizando el enfoque **Behavior Driven Development (BDD)** y sintaxis Gherkin.

Se contemplan:

- Inicio de sesión exitoso.
- Login con credenciales incorrectas.
- Validación de usuarios bloqueados.
- Validación de campos vacíos.

---

## 🛠️ Tecnologías utilizadas

| Tecnología         | Utilización                                                               |
| ------------------ | ------------------------------------------------------------------------- |
| Python 3.12        | Lenguaje utilizado para desarrollar las pruebas.                          |
| Pytest             | Framework para organizar y ejecutar pruebas automatizadas.                |
| Selenium WebDriver | Automatización e interacción con el navegador.                            |
| Google Chrome      | Navegador utilizado para las pruebas UI.                                  |
| Behave             | Framework BDD para ejecutar escenarios Gherkin.                           |
| pytest-html        | Generación de reportes HTML.                                              |
| Requests           | Cliente HTTP para pruebas de API, si corresponde a la suite implementada. |
| JSONPlaceholder    | API REST pública utilizada como entorno de pruebas..                      |
| Git / GitHub       | Control de versiones y alojamiento del proyecto.                          |
| GitHub Actions     | Integración continua y ejecución automática de pruebas.                   |

---

## 📁 Estructura del proyecto

```text
proyecto-final-automation-testing-luis-becerra/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── data/
│   ├── users.csv
│   └── products.json
│
├── features/
│   ├── steps/
│   │   └── login_steps.py
│   ├── environment.py
│   └── login.feature
│
├── logs/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── reports/
│   └── screenshots/
│
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_api.py
│
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   └── reader.py
│
├── conftest.py
├── pytest.ini
├── behave.ini
├── requirements.txt
└── README.md
```

### Descripción de las carpetas

- **data/**: almacena los datos utilizados para las pruebas, como credenciales y productos.
- **features/**: contiene los escenarios BDD escritos en Gherkin y sus correspondientes steps.
- **pages/**: implementa el patrón Page Object Model (POM), centralizando los elementos y acciones de cada página.
- **tests/**: contiene los casos de prueba automatizados con Pytest.
- **utils/**: reúne funciones reutilizables, como lectura de archivos y registro de logs.
- **reports/**: almacena los reportes generados y las capturas de pantalla de pruebas fallidas.
- **logs/**: almacena los registros de ejecución.
- **.github/workflows/**: contiene la configuración del pipeline de integración continua.

---

## 📦 Requisitos previos

Antes de ejecutar el proyecto, es necesario tener instalado:

- Python 3.12 o superior.
- Google Chrome.
- Git.
- Visual Studio Code (opcional, recomendado para trabajar con el proyecto).

Para verificar Python:

```bash
python --version
```

---

## 🚀 Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/Stevenzhunk/proyecto-final-automation-testing-luis-becerra.git
```

Ingresar a la carpeta:

```bash
cd proyecto-final-automation-testing-luis-becerra
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

Activar el entorno virtual en Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

Con el entorno virtual activado:

```bash
python -m pip install -r requirements.txt
```

El archivo `requirements.txt` contiene las dependencias necesarias para ejecutar el proyecto.

---

## ▶️ Ejecución de las pruebas con Pytest

Para ejecutar toda la suite de Pytest desde la carpeta raíz:

```bash
python -m pytest -s
```

El parámetro `-s` permite visualizar en la terminal los mensajes generados mediante `print()` durante la ejecución.

### Ejecutar pruebas por módulo

**Login:**

```bash
python -m pytest -s -m login
```

**Catálogo:**

```bash
python -m pytest -s -m catalogo
```

**Productos y carrito:**

```bash
python -m pytest -s -m productos
```

Los marcadores permiten ejecutar grupos específicos de pruebas sin necesidad de ejecutar toda la suite.

---

## 🥒 Ejecución de pruebas BDD con Behave

Para ejecutar los escenarios BDD del archivo de login:

```bash
python -m behave features/login.feature
```

Los escenarios están definidos en archivos `.feature` utilizando sintaxis Gherkin y se vinculan con las funciones implementadas en `features/steps/`.

---

## 🌐 Ejecución de pruebas API

Para ejecutar las pruebas automatizadas sobre JSONPlaceholder:

```bash
python -m pytest -s tests/test_api.py
```

Estas pruebas permiten verificar el comportamiento de diferentes métodos HTTP:

| Método HTTP | Operación                              | Resultado esperado |
| ----------- | -------------------------------------- | ------------------ |
| GET         | Consultar una publicación.             | HTTP 200           |
| POST        | Crear una publicación.                 | HTTP 201           |
| DELETE      | Eliminar una publicación.              | HTTP 200           |
| GET         | Consultar una publicación inexistente. | HTTP 404           |

Para generar un reporte HTML independiente de las pruebas API:

```bash
python -m pytest tests/test_api.py --html=reports/reporte_api.html --self-contained-html
```

**Nota:** JSONPlaceholder es una API de prueba que simula las operaciones de escritura. Las solicitudes POST y DELETE no modifican permanentemente sus datos.

---

## 📊 Reportes de ejecución

### Reporte HTML de Pytest

Al ejecutar la suite de Pytest, se genera automáticamente un reporte HTML en:

```text
reports/reporte.html
```

El reporte permite consultar:

- Cantidad de pruebas ejecutadas.
- Pruebas aprobadas y fallidas.
- Tiempo de ejecución.
- Detalle de errores.
- Información adicional de cada prueba.

Para generar un reporte independiente:

```bash
python -m pytest -s --html=reports/reporte_api.html --self-contained-html
```

### Capturas de pantalla

Cuando una prueba de interfaz gráfica falla, el proyecto captura automáticamente una imagen del navegador.

Las capturas se almacenan en:

```text
reports/screenshots/
```

Estas imágenes permiten analizar visualmente el estado de la aplicación al momento del fallo.

### Logs

Los registros de ejecución se almacenan en:

```text
logs/
```

Permiten consultar información sobre la ejecución y facilitar el diagnóstico de errores.

### Reporte JSON de Behave

En la ejecución configurada para GitHub Actions se genera un reporte JSON:

```text
reports/behave-report.json
```

Este archivo contiene información estructurada sobre los escenarios, pasos y resultados de las pruebas BDD.

---

## ⚙️ Integración continua - GitHub Actions

El proyecto incorpora un workflow de GitHub Actions que permite ejecutar las pruebas automáticamente cuando se realiza un `push` o un `pull request` hacia la rama `main`.

El pipeline contempla:

1. Descarga del repositorio.
2. Configuración del entorno Python.
3. Instalación de Google Chrome.
4. Instalación de dependencias.
5. Ejecución de las pruebas automatizadas con Pytest.
6. Ejecución de escenarios BDD con Behave.
7. Generación y almacenamiento de reportes como artefactos.

Los resultados pueden consultarse desde la pestaña **Actions** del repositorio de GitHub.

Los reportes generados se almacenan como artefactos descargables, permitiendo revisar los resultados de cada ejecución incluso después de finalizar el workflow.

---

## 🏷️ Pytest Marks

Las pruebas están organizadas mediante los siguientes marcadores:

| Marker      | Descripción                                                                          |
| ----------- | ------------------------------------------------------------------------------------ |
| `login`     | Automatización del inicio de sesión y verificación de la URL.                        |
| `catalogo`  | Navegación y verificación del catálogo.                                              |
| `productos` | Interacción con productos y carrito de compras.                                      |
| `api`       | Pruebas de endpoints HTTP mediante solicitudes GET, POST y DELETE a JSONPlaceholder. |

Para consultar los marcadores disponibles:

```bash
python -m pytest --markers
```

---

## 🧩 Buenas prácticas aplicadas

- Page Object Model (POM).
- Separación entre datos, lógica de pruebas y elementos de interfaz.
- Reutilización de funciones y métodos.
- Uso de esperas explícitas con WebDriverWait.
- Parametrización de pruebas.
- Organización de escenarios BDD con Gherkin.
- Registro de logs y capturas ante fallos.
- Integración continua mediante GitHub Actions.

---

## 🔗 Repositorio

[proyecto-final-automation-testing-luis-becerra](https://github.com/Stevenzhunk/proyecto-final-automation-testing-luis-becerra)
