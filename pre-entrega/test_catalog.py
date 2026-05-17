from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def dlogged(login_driver):
    driver = login_driver
    return driver

def test_catalog_tittle(dlogged):
    titulo = dlogged.title
    assert titulo == "Swag Labs", "El titulo de la pagina no es correcto"

def test_catalog_productos(dlogged):
    inventory_list = dlogged.find_elements(By.CLASS_NAME,"inventory_item")
    assert len(inventory_list) > 0
