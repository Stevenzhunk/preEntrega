
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


@given('que el usuario se encuentre en la pagina del login')
def step_abrir_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.abrir_pagina()


@when('ingresa en los campos de datos "{usuario}" y "{password}"')
def step_ingresar_credenciales(context, usuario, password):

    if usuario == "VACIO":
        usuario = ""

    if password == "VACIO":
        password = ""

    context.login_page.ingresar_usuario(usuario)
    context.login_page.ingresar_contrasena(password)


@when('hace click en el boton de login')
def step_click_login(context):
    context.login_page.hacer_click_login()


@then('deberia ingresar al inventario')
def step_verificar_inventario(context):

    WebDriverWait(context.driver, 15).until(
        EC.url_contains("/inventory.html")
    )

    WebDriverWait(context.driver, 15).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    productos = context.driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    assert len(productos) > 0


@then('deberia mostrarse el mensaje de error "{mensaje}"')
def step_verificar_error(context, mensaje):

    mensaje_obtenido = context.login_page.obtener_mensaje_error()

    assert mensaje_obtenido == mensaje, (
        f"Se esperaba: {mensaje}\n"
        f"Se obtuvo: {mensaje_obtenido}"
    )
