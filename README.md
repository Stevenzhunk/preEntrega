# 🧪 Automatización de Pruebas - SauceDemo

Proyecto de **QA Automation** desarrollado para automatizar pruebas funcionales sobre la aplicación web **SauceDemo**.

El proyecto utiliza **Python, Pytest y Selenium WebDriver** para validar diferentes funcionalidades de la aplicación mediante pruebas automatizadas ejecutadas en **Google Chrome**.

---

## 🎯 Propósito del proyecto

El objetivo del proyecto es automatizar diferentes escenarios funcionales de SauceDemo, aplicando herramientas y buenas prácticas de automatización de pruebas.

Las pruebas están organizadas en tres grupos principales (para Pre-entrega):

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

# 🛠️ Tecnologías utilizadas

| Tecnología             | Utilización                                     |
| ---------------------- | ----------------------------------------------- |
| **Python 3.12**        | Lenguaje utilizado para desarrollar las pruebas |
| **Pytest**             | Framework para crear y ejecutar las pruebas     |
| **Selenium WebDriver** | Automatización e interacción con el navegador   |
| **Google Chrome**      | Navegador utilizado para ejecutar las pruebas   |
| **pytest-html**        | Generación de reportes HTML                     |
| **Git**                | Control de versiones                            |

---

# 📦 Dependencias

El proyecto utiliza las siguientes dependencias de Python:

- pytest
- selenium
- pytest-html

---

🚀 Instalación

1. Requisitos previos

   Antes de ejecutar el proyecto es necesario tener instalado:

   Python 3.12 o superior.
   Google Chrome (si se desea usar este explorador, se puede ajustar en el fixture de browser() ).
   Git, si el proyecto será clonado desde un repositorio.

   Para verificar que Python está instalado:

   python --version

   El resultado esperado será similar a:

   Python 3.12.10

2. Crear un entorno virtual

   Se recomienda utilizar un entorno virtual para mantener aisladas las dependencias del proyecto.

   Desde la carpeta preEntrega ejecutar:

   python -m venv .venv
   Activar el entorno virtual en Windows

   En PowerShell:

   .venv\Scripts\Activate.ps1

   Una vez activado, la terminal debería mostrar el entorno virtual activo.

3. Instalar las dependencias

   Instalar Pytest:

   pip install pytest

   Instalar Selenium:

   pip install selenium

   Instalar pytest-html para generar reportes:

   pip install pytest-html

   También es posible instalar todas las dependencias en un solo comando:

   pip install pytest selenium pytest-html

   Para verificar que Pytest está instalado correctamente:

   pytest --version

   Para verificar Selenium:

   pip show selenium

   Para verificar pytest-html:

   pip show pytest-html

▶️ Ejecución de las pruebas:

    Para ejecutar todas las pruebas del proyecto, ubicarse dentro de la carpeta preEntrega y ejecutar:

      python -m pytest -s

    El parámetro -s permite visualizar en la terminal los mensajes generados mediante print() durante las pruebas.

🔐 Ejecutar solamente las pruebas de Login

      Para ejecutar únicamente la prueba de login:

      python -m pytest -s -m login

      Esta prueba verifica:

      Login exitoso.
      URL correcta después del login.

📋 Ejecutar solamente las pruebas del catálogo

      Para ejecutar únicamente las pruebas relacionadas con el catálogo:

      python -m pytest -s -m catalogo

      Esta prueba verifica:

      Título de la aplicación.
      Menú hamburguesa.
      Filtros.
      Productos disponibles.

🛒 Ejecutar solamente las pruebas de productos

      Para ejecutar únicamente la prueba de interacción con productos:

      python -m pytest -s -m productos

      Esta prueba verifica:

      Primer producto del catálogo.
      Nombre y precio.
      Agregado al carrito.
      Contador del carrito.
      Producto dentro del carrito.
      Coincidencia entre el producto agregado y el producto mostrado en el carrito.

🏷️ Pytest Marks

      Las pruebas están organizadas mediante los siguientes markers:

      Marker	Descripción
      login	Automatización del login y verificación de URL
      catalogo	Navegación y verificación del catálogo
      productos	Interacción con productos y carrito

      Los markers permiten ejecutar grupos específicos de pruebas sin necesidad de ejecutar todo el conjunto.

      Para visualizar los markers disponibles:

      python -m pytest --markers

📊 Generación de reportes HTML

      El proyecto utiliza pytest-html para generar reportes de las pruebas.

      Para ejecutar todas las pruebas y generar un reporte HTML:

      python -m pytest -s --html=reports/report.html

      El reporte será generado en:

      reports/report.html

      El archivo puede abrirse directamente desde un navegador para visualizar el resultado de la ejecución.

⏱️ Esperas explícitas

      Para mejorar la estabilidad de las pruebas, se utilizan esperas explícitas mediante WebDriverWait y expected_conditions.

      Por ejemplo:

      WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

      Estas esperas permiten que Selenium aguarde hasta que un determinado elemento esté disponible antes de continuar con la prueba, evitando depender de tiempos de espera fijos.
