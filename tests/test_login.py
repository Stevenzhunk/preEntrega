
import pytest

from pages.login_page import LoginPage
from utils.reader import read_users_csv
from utils.logger import logger

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.login
@pytest.mark.parametrize("data", read_users_csv())
def test_login(driver, data):

    try:
        logger.info(f"Iniciando prueba de login para: {data['usuario']}")

        login_page = LoginPage(driver)

        logger.info("Abriendo la página de login.")
        login_page.login_saucedemo(
            data["usuario"],
            data["password"]
        )

        logger.info("Credenciales enviadas correctamente.")

        if data["tipo_usuario"] == "exitoso":

            logger.info("Verificando acceso al inventario.")

            WebDriverWait(driver, 10).until(
                EC.url_contains("/inventory.html")
            )

            assert "/inventory.html" in driver.current_url

            logger.info("Login exitoso.")

        else:

            logger.info("Verificando mensaje de error.")

            error = login_page.obtener_mensaje_error()

            assert "Epic sadface" in error

            if data["tipo_usuario"] == "bloqueado":
                assert "locked out" in error.lower()
                logger.info("Usuario bloqueado validado correctamente.")

            else:
                assert "Username and password do not match" in error
                logger.info("Credenciales inválidas validadas correctamente.")

    except Exception:
        logger.exception(
            f"Error durante la prueba de login para: {data['usuario']}"
        )
        raise
