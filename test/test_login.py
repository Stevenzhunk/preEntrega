from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

def test_login_exitoso():
  #seleccionar Webdriver
  driver = webdriver.Chrome()

  #abrir Web
  driver.get("https://www.saucedemo.com/")

  #Encontrar Elementos
  user = driver.find_element(By.ID, "user-name")
  password = driver.find_element(By.ID, "password")
  button = driver.find_element(By.ID, "login-button")

  #completar el formulario
  user.send_keys("standard_user")
  password.send_keys("secret_sauce")

  #esperar tiempo
  time.sleep(1)

  #click login
  button.click()

  #Encontrar endpoint url 
  assert driver.current_url == "https://www.saucedemo.com/inventory.html"

  titulo= driver.find_element (By.CSS_SELECTOR, ".header_label >.app_logo").text

  #checkear el titulo de la pagina
  assert titulo== "Swag Labs" 

  #Cerrar Explorador
  driver.quit()
