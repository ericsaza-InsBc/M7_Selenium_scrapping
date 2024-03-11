from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

page = "llardelllibre"

# Función que busca el precio de un libro en Agapea
def buscar_precio_libro(isbn):

    # Instanciamos un driver
    driver = webdriver.Firefox()

    # Maximizamos la ventana
    driver.maximize_window()

    # Abre la página necesaria
    if (page == "agapea"):
        driver.get(f"https://www.agapea.com/poesies-{isbn}-i.htm")

        # Espera a que la página cargue
        time.sleep(4)

        # Aceptamos las cookies
        driver.find_element(By.XPATH, "//button[@id='cookie-accept']").click()
        
        # Espera a que se quite el alert
        time.sleep(4)

        # Obtenemos el nombre
        nombre_producto = driver.find_element(By.XPATH, "//div[@class='datos-libro']/div/h1").text

        # Obtenemos el precio
        precio_producto = driver.find_element(By.XPATH, "//strong[1]").text.replace("€", "").replace(",", ".").strip()

        # Obtenemos el ISBN13
        isbn13 = driver.find_element(By.XPATH, "//tbody/tr[6]/td[1]/b[1]").text

        # Obtenemos el elemento de las existencias
        existencias = 'no available' if driver.find_element(By.CSS_SELECTOR, "div[class='etiqueta']").text == "SIN EXISTENCIAS" else 'available'

    elif (page == "llardelllibre"):
        driver.get(f"https://www.llardelllibre.cat/cat/")

        # Espera a que la página cargue
        time.sleep(4)

        # Escribimos el ISBN en el buscador
        driver.find_element(By.XPATH, "//input[@placeholder='Títol, autor o ISBN']").send_keys(isbn)

        # Hacemos click en el botón de buscar
        driver.find_element(By.XPATH, "//button[@title='Buscar']").click()
        
        # Obtenemos el nombre
        nombre_producto = driver.find_element(By.XPATH, "//dd[@class='title']/a").text
        
        # Obtenemos el precio
        precio_producto = driver.find_element(By.CSS_SELECTOR, "p[class='precio'] strong").text.replace("€", "").replace(",", ".").strip()

        # Obtenemos el ISBN13
        isbn13 = isbn

        # Obtenemos el elemento de las existencias
        existencias = 'no available' if driver.find_element(By.XPATH, "//dd[@class='disponibilidad orange']").text == "Sense estoc, consultar termini entrega" else 'available'

    # Creamos un diccionario con la información
    infoLlibre = {  
        "EAN13": isbn13,
        "ecommerce": page,
        "name" : nombre_producto,
        "status": existencias,
        "price": None if existencias == 'no available' else precio_producto
    }

    # Imprimimos la información
    print(infoLlibre)

    # Cerramos el navegador
    driver.quit()


# Uso de la función con un ISBN específico
isbn = "9788418928949"
isbn2 = "9788482649498"
buscar_precio_libro(isbn)
# print("-------------------------------------------------")
# buscar_precio_libro(isbn2)