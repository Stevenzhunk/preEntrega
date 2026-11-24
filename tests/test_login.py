from pages.login_page import LoginPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger

def test_login_exitoso(driver):

    # Instanciar la página de login
    logger.info("Iniciando prueba de login exitoso.")
    login_page = LoginPage(driver)

    # Iniciar sesión
    logger.info("Iniciando sesión con usuario estándar.")
    login_page.login_saucedemo("standard_user", "secret_sauce")

    logger.info("Verificando que la URL contenga '/inventory.html'.")
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in driver.current_url