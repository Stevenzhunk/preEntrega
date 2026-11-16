from pages.login_page import LoginPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_exitoso(browser):

    # Instanciar la página de login
    login_page = LoginPage(browser)

    # Iniciar sesión
    login_page.login_saucedemo("standard_user", "secret_sauce")

    # Verificar que se haya ingresado al inventario
    WebDriverWait(browser, 10).until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in browser.current_url