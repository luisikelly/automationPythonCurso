from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def dlogged(login_driver):
    driver = login_driver
    return driver

def test_add_cart(dlogged):
    # Agregar prodcucto al carrito
    dlogged.find_elements(By.CLASS_NAME, "btn_inventory")[0].click() 
    # Verificar contador carrito
    contador_cart = dlogged.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert contador_cart.text == "1", "No se agrego producto al carrito"

def test_item_cart(dlogged):
    product = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    # Verificar el producto agregado en el carrito
    assert cart_item == product_name, "El producto en el carrito no coincide con el seleccionado"