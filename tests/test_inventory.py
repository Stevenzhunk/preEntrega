import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger

@pytest.mark.catalogo
def test_inventory(driver):

    logger.info("Iniciando prueba de inventario.")
    login_page = LoginPage(driver)
    
    logger.info("Iniciando sesión con usuario estándar.")
    login_page.login_saucedemo("standard_user", "secret_sauce")

    logger.info("Instanciando la página de inventario.")
    inventory_page = InventoryPage(driver)

    logger.info("Obteniendo nombre y precio del primer producto del inventario.")
    first_product_name = inventory_page.obtener_nombre_primer_producto()
    first_product_price = inventory_page.obtener_precio_primer_producto()
 
    logger.info("Verificando que el título de la página sea 'Swag Labs' y que haya productos en el inventario.")
    assert inventory_page.obtener_titulo() == "Swag Labs"
    assert len(inventory_page.obtener_productos()) > 0
    logger.info(f"Se encontraron {len(inventory_page.obtener_productos())} productos en el inventario.")
    

    logger.info(f"El primer producto del catalogo es: {first_product_name}")
    logger.info(f"El precio del primer producto es: {first_product_price}")

    assert first_product_name == "Sauce Labs Backpack"
    assert first_product_price == "$29.99"

    assert inventory_page.menu_visible()
    assert inventory_page.filtro_visible()

