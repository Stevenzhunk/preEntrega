from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_saucedemo(driver, username="standard_user", password="secret_sauce"):
    # Encontrar elementos
    user = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    button = driver.find_element(By.ID, "login-button")

    # Completar formulario
    user.send_keys(username)
    password_field.send_keys(password)

    # Click en Login
    button.click()

    # Esperar hasta que cargue la página de inventario
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header_label > .app_logo")))
