from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login(login_driver):
    login_driver.get("https://www.saucedemo.com/")
    
    # Completar credenciales
    username = login_driver.find_element(By.XPATH, "//*[@id='user-name']")
    username.send_keys("standard_user")
    password = login_driver.find_element(By.XPATH, "//*[@id='password']")
    password.send_keys("secret_sauce")
    # Click en login
    login_driver.find_element(By.XPATH, "//*[@id='login-button']").click()
    
    # Verificar que el login fue exitoso
    assert "/inventory.html" in login_driver.current_url, "No se redirigio al catalogo de la pagina"