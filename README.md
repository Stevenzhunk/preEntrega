# 🧪 Automatización de Pruebas - SauceDemo

Proyecto de **QA Automation** desarrollado para automatizar pruebas funcionales sobre la aplicación web **SauceDemo**.

El proyecto utiliza **Python, Pytest y Selenium WebDriver** para validar diferentes funcionalidades de la aplicación mediante pruebas automatizadas ejecutadas en **Google Chrome**.

---

## 🎯 Propósito del proyecto

El objetivo es automatizar diferentes escenarios funcionales de SauceDemo, aplicando herramientas y buenas prácticas de automatización de pruebas.

Las pruebas están organizadas en tres grupos principales correspondientes a la pre-entrega.

### 🔐 Automatización de Login

Se verifica:

- Acceso a la página de SauceDemo.
- Ingreso de usuario y contraseña.
- Inicio de sesión exitoso.
- Redirección correcta a la página del catálogo.

### 📋 Navegación y verificación del catálogo

Se verifica:

- Título de la aplicación.
- Menú hamburguesa.
- Filtros del catálogo.
- Existencia de productos disponibles.

### 🛒 Interacción con productos

Se verifica:

- Identificación del primer producto del catálogo.
- Obtención del nombre y precio del producto.
- Agregado del primer producto al carrito.
- Incremento del contador del carrito.
- Navegación hacia la página del carrito.
- Existencia del producto dentro del carrito.
- Comparación entre el producto agregado y el producto mostrado en el carrito.

---

## 🛠️ Tecnologías utilizadas

| Tecnología         | Utilización                                      |
| ------------------ | ------------------------------------------------ |
| Python 3.12        | Lenguaje utilizado para desarrollar las pruebas. |
| Pytest             | Framework para crear y ejecutar las pruebas.     |
| Selenium WebDriver | Automatización e interacción con el navegador.   |
| Google Chrome      | Navegador utilizado para ejecutar las pruebas.   |
| pytest-html        | Generación de reportes HTML.                     |
| Git                | Control de versiones.                            |

---

## 📦 Dependencias

El proyecto utiliza las siguientes dependencias de Python:

- `pytest`
- `selenium`
- `pytest-html`

---

## 🚀 Instalación y configuración

### 1. Requisitos previos

Antes de ejecutar el proyecto, es necesario tener instalado:

- **Python 3.12 o superior.**
- **Google Chrome**, navegador utilizado para ejecutar las pruebas.
- **Git**, si el proyecto se obtiene mediante un repositorio.

Para verificar que Python está instalado correctamente, ejecutar:

```bash
python --version
```

El resultado esperado será similar a:

```text
Python 3.12.10
```

### 2. Crear un entorno virtual

Se recomienda utilizar un entorno virtual para mantener aisladas las dependencias del proyecto.

Desde la carpeta raíz `preEntrega`, ejecutar:

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

En Windows, utilizando PowerShell, ejecutar:

```powershell
.venv\Scripts\Activate.ps1
```

Una vez activado, la terminal debería mostrar el nombre del entorno virtual activo.

### 4. Instalar las dependencias

Con el entorno virtual activado, instalar las dependencias necesarias:

```bash
pip install pytest selenium pytest-html
```

También es posible instalarlas por separado:

```bash
pip install pytest
```

```bash
pip install selenium
```

```bash
pip install pytest-html
```

Para verificar que Pytest está instalado correctamente:

```bash
pytest --version
```

Para consultar la instalación de Selenium:

```bash
pip show selenium
```

Para consultar la instalación de pytest-html:

```bash
pip show pytest-html
```

---

## ▶️ Ejecución de las pruebas

Para ejecutar las pruebas, ubicarse en la carpeta raíz `preEntrega`, donde se encuentra el archivo `pytest.ini`.

Ejecutar el siguiente comando:

```bash
python -m pytest -s
```

El parámetro `-s` permite visualizar en la terminal los mensajes generados mediante `print()` durante la ejecución de las pruebas.

---

## 🔐 Ejecutar solamente las pruebas de Login

Para ejecutar únicamente las pruebas identificadas con el marcador `login`:

```bash
python -m pytest -s -m login
```

Esta prueba verifica:

- Inicio de sesión exitoso.
- Redirección a la URL correcta después del login.

---

## 📋 Ejecutar solamente las pruebas del catálogo

Para ejecutar únicamente las pruebas relacionadas con el catálogo:

```bash
python -m pytest -s -m catalogo
```

Estas pruebas verifican:

- Título de la aplicación.
- Menú hamburguesa.
- Filtros del catálogo.
- Disponibilidad de productos.

---

## 🛒 Ejecutar solamente las pruebas de productos

Para ejecutar únicamente las pruebas de interacción con productos:

```bash
python -m pytest -s -m productos
```

Estas pruebas verifican:

- Identificación del primer producto del catálogo.
- Obtención del nombre y precio.
- Agregado del producto al carrito.
- Actualización del contador del carrito.
- Presencia del producto dentro del carrito.
- Coincidencia entre el producto agregado y el producto mostrado en el carrito.

---

## 🏷️ Pytest Marks

Las pruebas están organizadas mediante los siguientes marcadores (_markers_):

| Marker      | Descripción                                                   |
| ----------- | ------------------------------------------------------------- |
| `login`     | Automatización del inicio de sesión y verificación de la URL. |
| `catalogo`  | Navegación y verificación del catálogo.                       |
| `productos` | Interacción con productos y carrito de compras.               |

Los markers permiten ejecutar grupos específicos de pruebas sin necesidad de ejecutar toda la suite.

Para visualizar los marcadores disponibles:

```bash
python -m pytest --markers
```

---

## 📊 Generación de reportes HTML

El proyecto utiliza `pytest-html` para generar reportes HTML con los resultados de la ejecución de las pruebas.

Para ejecutar todas las pruebas y generar un reporte, utilizar:

```bash
python -m pytest -s --html=reports/report.html
```

El reporte se generará en la siguiente ubicación:

`reports/report.html`

El archivo puede abrirse directamente desde un navegador para consultar los resultados de la ejecución.

### Generar un reporte ejecutando un grupo específico

También es posible generar reportes de grupos individuales de pruebas.

**Ejemplo: reporte de las pruebas de Login**

```bash
python -m pytest -s -m login --html=reports/login.html
```

**Ejemplo: reporte de las pruebas del catálogo**

```bash
python -m pytest -s -m catalogo --html=reports/catalogo.html
```

**Ejemplo: reporte de las pruebas de productos**

```bash
python -m pytest -s -m productos --html=reports/productos.html
```

---

## ⏱️ Esperas explícitas

Para mejorar la estabilidad de las pruebas, se utilizan esperas explícitas mediante `WebDriverWait` y `expected_conditions`, herramientas proporcionadas por Selenium.

Ejemplo de espera explícita:

```python
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
)
```

Esta espera permite que Selenium aguarde hasta un máximo de 10 segundos para que el elemento indicado esté presente en el DOM antes de continuar con la prueba.

El uso de esperas explícitas ayuda a reducir errores ocasionados por diferencias en los tiempos de carga de la aplicación y evita depender exclusivamente de pausas fijas mediante `time.sleep()`.

---
