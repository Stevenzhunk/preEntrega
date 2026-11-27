
import os
from selenium import webdriver


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()

    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")

    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
