from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pytest


# Fixture para el driver (se ejecuta antes de cada test)
@pytest.fixture(scope="function")
def driver():
    # Usando webdriver-manager para no descargar drivers manualmente
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Descomenta para modo sin interfaz

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver
    driver.quit()


def test_login_exitoso(driver):
    driver.get("https://www.saucedemo.com/")
    
    # Completar credenciales
    username = wait.until(driver.find_element(By.XPATH, "//*[@id="user-name"]"))
    username.send_keys("standard_user")
    password = driver.find_element(By.XPATH, "//*[@id="password"]")
    password.send_keys("secret_sauce")
    
    # Click en login
    driver.find_element(By.XPATH, "//*[@id="login-button"]").click()
    
    # Verificar que el login fue exitoso
    assert "You logged into a secure area!" in success_message.text
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
