import pytest
from selenium import webdriver

@pytest.fixture
def browser():
  # Configuración del navegador Chrome
  driver = webdriver.Chrome()
  driver.implicitly_wait(10)  # Espera implícita de 10 segundos

  driver.get("https://www.saucedemo.com/")

  yield driver

  driver.quit()