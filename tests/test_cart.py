
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger
from utils.reader import read_productos_json


@pytest.mark.parametrize("producto", read_productos_json())
def test_carrito(driver, producto):

    logger.info(f"Iniciando prueba de carrito para: {producto['nombre']}")

    login_page = LoginPage(driver)
    login_page.login_saucedemo("standard_user", "secret_sauce")

    
    logger.info("Instanciando la página de inventario.")
    inventory_page = InventoryPage(driver)

    
    logger.info(f"Agregando '{producto['nombre']}' del JSON al carrito.")
    inventory_page.agregar_producto(producto["nombre"])

    
    logger.info("Verificando contador del carrito.")
    assert inventory_page.obtener_contador_carrito() == "1"

    
    logger.info("Navegando al carrito de compras.")
    inventory_page.ir_al_carrito()

    
    cart_page = CartPage(driver)

    logger.info("Esperando a que la URL del carrito sea correcta.")
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/cart.html")
    )

    assert driver.current_url == "https://www.saucedemo.com/cart.html"

    
    logger.info("Verificando título del carrito.")
    assert cart_page.obtener_titulo() == "Your Cart"

    logger.info("Obteniendo productos en el carrito.")
    cart_items = cart_page.obtener_productos_carrito()

    logger.info(f"El carrito contiene {len(cart_items)} productos.")
    assert cart_page.obtener_cantidad_productos() == 1

    logger.info("Verificando nombre del producto en el carrito.")
    cart_product_name = cart_page.obtener_nombre_producto(cart_items[0])

    logger.info(f"Producto encontrado en el carrito: {cart_product_name}")
    assert cart_product_name == producto["nombre"]

    logger.info("Verificando precio del producto en el carrito.")
    cart_product_price = cart_page.obtener_precio_producto(cart_items[0])

    logger.info(f"Precio del producto en el carrito: {cart_product_price}")
    assert cart_product_price == producto["precio"]

    logger.info(f"Prueba de carrito finalizada correctamente para: {producto['nombre']}")
