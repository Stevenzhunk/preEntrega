import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.saucedemo import login_saucedemo


@pytest.fixture
def browser():
    # Configuración del navegador Chrome
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()


@pytest.mark.login
def test_login_exitoso(browser):

    login_saucedemo(browser)

    # Verifica que la URL sea la correcta después del login
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"


@pytest.mark.catalogo
def test_navegacion_y_verificacion_catalogo(browser):

    login_saucedemo(browser)

    # Verifica que el título de la página sea "Swag Labs"
    titulo = browser.find_element(By.CSS_SELECTOR, ".header_label > .app_logo").text

    assert titulo == "Swag Labs"

    # Verifica que el menú hamburguesa esté visible
    menu = browser.find_element(By.ID, "react-burger-menu-btn")

    assert menu.is_displayed()

    # Verifica que los filtros estén visibles
    filtros = browser.find_element(By.CLASS_NAME, "product_sort_container")

    assert filtros.is_displayed()

    # Verifica que existan productos
    products = browser.find_elements(By.CLASS_NAME, "inventory_item")

    print(f"Se encontraron {len(products)} productos.")

    assert len(products) > 0


@pytest.mark.productos
def test_interaccion_productos(browser):

    login_saucedemo(browser)

    # Encontrar productos
    products = browser.find_elements(By.CLASS_NAME, "inventory_item")

    # Obtener nombre del primer producto
    first_product_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text

    print("El primer producto del catalogo es:", first_product_name)

    # Obtener precio del primer producto
    first_product_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text

    print("El precio del primer producto es:", first_product_price)

    # Encontrar el botón del primer producto
    add_button = products[0].find_element(By.CLASS_NAME, "btn_inventory")

    # Esperar hasta que el botón esté disponible
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory")))

    # Agregar el primer producto al carrito
    add_button.click()

    # Esperar hasta que el contador del carrito tenga el valor 1
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1"))

    cart = browser.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    print(f"El carrito tiene {cart} productos.")

    assert cart == "1"

    # Ir a la página del carrito
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Esperar hasta que cargue la URL del carrito
    WebDriverWait(browser, 10).until(EC.url_to_be("https://www.saucedemo.com/cart.html"))

    assert browser.current_url == "https://www.saucedemo.com/cart.html"

    # Esperar hasta que aparezca el producto en el carrito
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

    cart_items = browser.find_elements(By.CLASS_NAME, "cart_item")

    print(f"El carrito en su web tiene {len(cart_items)} productos.")

    assert len(cart_items) == 1

    # Obtener nombre del producto en el carrito
    cart_product_name = cart_items[0].find_element(By.CLASS_NAME, "inventory_item_name").text

    print("El primer producto en la pagina del carrito es:", cart_product_name)

    # Verificar que sea el mismo producto agregado
    assert cart_product_name == first_product_name