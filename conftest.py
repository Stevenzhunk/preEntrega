import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Configuración del navegador Chrome
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    yield driver

    # Cerrar navegador al finalizar la prueba
    driver.quit()