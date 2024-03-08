from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Función que busca el precio de un libro en Agapea
def buscar_precio_libro(isbn):

    # Instanciamos un driver
    driver = webdriver.Firefox()

    # Maximizamos la ventana
    driver.maximize_window()

    # Abre la página de Agapea
    driver.get(f"https://www.agapea.com/poesies-{isbn}-i.htm")

    # Espera a que la página cargue
    time.sleep(4)

    # Aceptamos las cookies
    driver.find_element(By.XPATH, "//button[normalize-space()='Aceptar cookies']").click()
    
    # Espera a que la página cargue
    time.sleep(4)

    # Obtenemos el nombre
    nombre_producto = driver.find_element(By.XPATH, "//div[@class='datos-libro']/div/h1").text

    # Obtenemos el precio
    precio_producto = driver.find_element(By.XPATH, "//strong[1]").text

    print(f"El nombre del producto es: {nombre_producto}")
    print(f"El precio del producto és: {precio_producto}")

    # Cerramos el navegador
    driver.quit()


# Uso de la función con un ISBN específico
isbn = "9788418928949"
buscar_precio_libro(isbn)
