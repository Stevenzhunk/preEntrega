
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_carrito(driver):

    # Iniciar sesión
    login_page = LoginPage(driver)
    login_page.login_saucedemo("standard_user", "secret_sauce")

    # Instanciar página de inventario
    inventory_page = InventoryPage(driver)

    # Obtener nombre del primer producto
    first_product_name = inventory_page.obtener_nombre_primer_producto()

    # Agregar producto al carrito
    inventory_page.agregar_producto(first_product_name)

    # Verificar contador del carrito
    assert inventory_page.obtener_contador_carrito() == "1"

    # Ir al carrito
    inventory_page.ir_al_carrito()

    # Instanciar página del carrito
    cart_page = CartPage(driver)

    # Verificar URL del carrito
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/cart.html")
    )

    assert driver.current_url == "https://www.saucedemo.com/cart.html"

    # Verificar título del carrito
    assert cart_page.obtener_titulo() == "Your Cart"

    # Obtener productos del carrito
    cart_items = cart_page.obtener_productos_carrito()

    print(f"El carrito en su web tiene {len(cart_items)} productos.")

    assert cart_page.obtener_cantidad_productos() == 1

    # Obtener nombre del producto en el carrito
    cart_product_name = cart_page.obtener_nombre_producto(cart_items[0])

    print("El primer producto en la pagina del carrito es:", cart_product_name)

    # Verificar que sea el mismo producto agregado
    assert cart_product_name == first_product_name
