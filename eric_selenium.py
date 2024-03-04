from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Instanciamos un driver
driver = webdriver.Firefox()

# Abre la página de Amazon
driver.get("https://www.amazon.es/s?k=9788418928949")

# Espera a que la página cargue
time.sleep(5)

# Clickamos al botón para aceptar las cookies
driver.find_element(By.XPATH, "//*[@id='sp-cc-accept']").click()

# Espera a que se vea todo
time.sleep(5)
# Obtenemos el precio
precio_producto = driver.find_elements(By.XPATH, "//span[@class='a-offscreen']")[0].get_attribute('innerHTML').replace("&nbsp;", "")
print(f'El precio del producto és: {precio_producto}')

# Cerramos el navegador
driver.quit()