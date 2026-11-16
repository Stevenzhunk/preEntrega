
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_inventory(driver):

    # Iniciar sesión
    login_page = LoginPage(driver)
    login_page.login_saucedemo("standard_user", "secret_sauce")

    # Instanciar página de inventario
    inventory_page = InventoryPage(driver)

    # Obtener información del primer producto
    first_product_name = inventory_page.obtener_nombre_primer_producto()
    first_product_price = inventory_page.obtener_precio_primer_producto()
 

    assert inventory_page.obtener_titulo() == "Swag Labs"
    assert len(inventory_page.obtener_productos()) > 0

    print("El primer producto del catalogo es:", first_product_name)
    print("El precio del primer producto es:", first_product_price)

    assert first_product_name == "Sauce Labs Backpack"
    assert first_product_price == "$29.99"

    assert inventory_page.menu_visible()
    assert inventory_page.filtro_visible()

