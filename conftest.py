
import pytest
from selenium import webdriver
import pytest_html
import pathlib
import base64

# Guardar URL y capturar pantalla si falla la prueba
@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")

    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()


# Guardar URL y capturar pantalla si falla la prueba
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("driver")

        if driver:
            report.page_url = driver.current_url

            if report.failed:
                carpeta = pathlib.Path("reports/screenshots")
                carpeta.mkdir(parents=True, exist_ok=True)

                archivo = carpeta / f"{item.name}.png"
                driver.save_screenshot(str(archivo))

                imagen = base64.b64encode(
                    archivo.read_bytes()
                ).decode("utf-8")

                report.extras = [
                    pytest_html.extras.png(imagen, name="Screenshot")
                ]


# Encabezado del reporte
def pytest_html_results_table_header(cells):
    cells.insert(3, "URL")


# URL en cada fila
def pytest_html_results_table_row(report, cells):
    cells.insert(3, getattr(report, "page_url", "-"))
