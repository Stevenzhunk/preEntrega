from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login_exitoso():

    # Abrir Chrome
    driver = webdriver.Chrome()

    # Abrir página
    driver.get("https://www.saucedemo.com/")

    # Encontrar elementos
    user = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    button = driver.find_element(By.ID, "login-button")

    # Completar formulario
    user.send_keys("standard_user")
    password.send_keys("secret_sauce")

    # Esperar tiempo
    time.sleep(2)

    # Click en Login
    button.click()

    # Verificar URL
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    # Verificar título
    titulo = driver.find_element(By.CSS_SELECTOR, ".header_label > .app_logo").text
    assert titulo == "Swag Labs"

    # Verificar filtros
    filtros = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtros.is_displayed()

    #verificar Boton Hamburgesa 
    menu = driver.find_element(By.ID, "shopping_cart_container")
    assert menu.is_displayed()



    # Encontrar productos
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")

    # Mostrar cantidad de productos
    print(f"Se encontraron {len(products)} productos.")

    # Mostrar nombre del primer producto
    print("El primer producto es:", products[0].find_element(By.CLASS_NAME, "inventory_item_name").text)

    # Mostrar precio del primer producto
    print("El precio del primer producto es:", products[0].find_element(By.CLASS_NAME, "inventory_item_price").text)
    
    #click añadir al carrito el primer producto
    products[0].find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

    #Chekear que el carrito tiene 1 producto
    cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    print(f'El carrito tiene {cart} productos.')
    assert cart == '1'
    time.sleep(2)

    # Esperar tiempo
    time.sleep(2)

    # Cerrar navegador
    driver.quit()