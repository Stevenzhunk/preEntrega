
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    # Configuración del navegador Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


# Guardar la URL al finalizar cada prueba
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("driver")

        if driver:
            report.page_url = driver.current_url


# Personalizar encabezado del reporte HTML
# Personalizar encabezado del reporte HTML
def pytest_html_results_table_header(cells):
    cells.insert(3, "URL")


# Agregar URL a cada fila del reporte
def pytest_html_results_table_row(report, cells):
    cells.insert(3, getattr(report, "page_url", "-"))