
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        titulo = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[@class='title' and text()='Your Cart']")
            )
        )
        return titulo.text
    

    def obtener_productos_carrito(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "cart_item")
            )
        )

    def obtener_cantidad_productos(self):
        productos = self.obtener_productos_carrito()
        return len(productos)

    def obtener_nombre_producto(self, producto):
        return producto.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

    def continuar_comprando(self):
        boton = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue-shopping")
            )
        )
        boton.click()
        
    def obtener_precio_producto(self, producto):
        return producto.find_element(
            By.CLASS_NAME, "inventory_item_price"
        ).text
