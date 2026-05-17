# Proyecto de Automatización QA - Pre Entrega

## Descripción

Proyecto de automatización de pruebas funcionales realizado con **Python**, **Selenium WebDriver** y **Pytest**.  
El objetivo principal es automatizar distintas funcionalidades de una aplicación web para garantizar su correcto funcionamiento y garantizar la calidad del software.

---

## Tecnologías Utilizadas

- **Python**
- **Selenium WebDriver**
- **Pytest**
- **Pytest-HTML** (reportes)
- **Git** y **GitHub**

---

## Requisitos Previos

- Python 3.8 o superior instalado
- Git instalado
- Navegador Chrome (recomendado)

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/luisikelly/automationPythonCurso.git
cd pre-entrega
```
---

## Cómo Ejecutar las Pruebas
### Ejecutar todas las pruebas
```bash
pytest tests/ -v
```
### Ejecutar un test específico
```bash
pytest tests/test_login.py -v
```
--------------
## Funcionamiento de las Pruebas

- Test Login: Validación de login exitoso.
- Test Cart: Añadir producto al carrito y validacion del producto agregado.
- Test Catalog: Navegación por catalogo de productos en la pantalla principal de la pagina
