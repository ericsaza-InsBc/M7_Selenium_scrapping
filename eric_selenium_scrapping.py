from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

page = "llardelllibre"

# Funció que busca el preu d'un llibre a Agapea
def buscar_precio_libro(isbn):

    # Instanciem un driver
    driver = webdriver.Firefox()

    # Maximizem la finestra
    driver.maximize_window()

    # Obre la pàgina necessària
    if (page == "agapea"):
        driver.get(f"https://www.agapea.com/poesies-{isbn}-i.htm")

        # Espera que la pàgina carregui
        time.sleep(4)

        # Acceptem les cookies
        driver.find_element(By.XPATH, "//button[@id='cookie-accept']").click()
        
        # Espera que desaparegui l'alerta
        time.sleep(4)

        # Obtenim el nom
        nombre_producto = driver.find_element(By.XPATH, "//div[@class='datos-libro']/div/h1").text

        # Obtenim el preu
        precio_producto = driver.find_element(By.XPATH, "//strong[1]").text.replace("€", "").replace(",", ".").strip()

        # Obtenim l'ISBN13
        isbn13 = driver.find_element(By.XPATH, "//tbody/tr[6]/td[1]/b[1]").text

        # Obtenim l'element de les existencias
        existencias = 'no available' if driver.find_element(By.CSS_SELECTOR, "div[class='etiqueta']").text == "SIN EXISTENCIAS" else 'available'

    elif (page == "llardelllibre"):
        driver.get(f"https://www.llardelllibre.cat/cat/")

        # Espera que la pàgina carregui
        time.sleep(4)

        # Escrivim l'ISBN al cercador
        driver.find_element(By.XPATH, "//input[@placeholder='Títol, autor o ISBN']").send_keys(isbn)

        # Cliquem al botó de cercar
        driver.find_element(By.XPATH, "//button[@title='Buscar']").click()
        
        # Obtenim el nom
        nombre_producto = driver.find_element(By.XPATH, "//dd[@class='title']/a").text
        
        # Obtenim el preu
        precio_producto = driver.find_element(By.CSS_SELECTOR, "p[class='precio'] strong").text.replace("€", "").replace(",", ".").strip()

        # Obtenim l'ISBN13
        isbn13 = isbn

        # Obtenim l'element de les existencias
        existencias = 'no available' if driver.find_element(By.XPATH, "//dd[@class='disponibilidad orange']").text == "Sense estoc, consultar termini entrega" else 'available'

    # Creem un diccionari amb la informació
    infoLlibre = {  
        "EAN13": isbn13,
        "ecommerce": page,
        "name" : nombre_producto,
        "status": existencias,
        "price": None if existencias == 'no available' else precio_producto
    }

    # Imprimim
    print(infoLlibre)

    # Tanquem el navegador
    driver.quit()


# Ús de la funció amb un ISBN específic
isbn = "9788418928949"
isbn2 = "9788482649498"
buscar_precio_libro(isbn)
# print("-------------------------------------------------")
# buscar_precio_libro(isbn2)