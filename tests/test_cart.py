
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


def test_carrito(driver):

    logger.info("Iniciando prueba de carrito.")
    login_page = LoginPage(driver)
    login_page.login_saucedemo("standard_user", "secret_sauce")

    logger.info("Instanciando la página de inventario.")
    inventory_page = InventoryPage(driver)

    logger.info("Obteniendo nombre del primer producto del inventario.")
    first_product_name = inventory_page.obtener_nombre_primer_producto()

    logger.info(f"Agregando el primer producto '{first_product_name}' al carrito.")
    inventory_page.agregar_producto(first_product_name)

    logger.info("Verificando que el contador del carrito sea '1'.")
    assert inventory_page.obtener_contador_carrito() == "1"

    logger.info("Navegando al carrito de compras.")
    inventory_page.ir_al_carrito()

    logger.info("Instanciando la página del carrito.")
    cart_page = CartPage(driver)

    logger.info("Verificando que la URL sea 'https://www.saucedemo.com/cart.html'.")    
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/cart.html")
    )

    assert driver.current_url == "https://www.saucedemo.com/cart.html"

    logger.info("Verificando que el título de la página del carrito sea 'Your Cart'.")
    assert cart_page.obtener_titulo() == "Your Cart"

    logger.info("Obteniendo productos en el carrito.")
    cart_items = cart_page.obtener_productos_carrito()

    logger.info(f"El carrito en su web tiene {len(cart_items)} productos.")

    assert cart_page.obtener_cantidad_productos() == 1

    logger.info("Obteniendo nombre del primer producto en la página del carrito.")
    cart_product_name = cart_page.obtener_nombre_producto(cart_items[0])

    logger.info(f"El primer producto en la pagina del carrito es: {cart_product_name}")

    logger.info("Verificando que el nombre del producto en el carrito coincida con el nombre del primer producto del inventario.")
    assert cart_product_name == first_product_name
