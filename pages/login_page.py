from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get("https://www.saucedemo.com/")

    def ingresar_usuario(self, username):
        user_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        user_field.send_keys(username)

    def ingresar_contrasena(self, password):
        password_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(password)

    def hacer_click_login(self):
        
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()

    def obtener_mensaje_error(self):
        error_message = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "h3[data-test='error']")
            )
        )
        return error_message.text

    def login_saucedemo(self, username, password):
        self.abrir_pagina()
        self.ingresar_usuario(username)
        self.ingresar_contrasena(password)
        self.hacer_click_login()