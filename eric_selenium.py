from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Instanciamos un driver
driver = webdriver.Firefox()

# Maximizamos la ventana
driver.maximize_window()

# Abre la página de Amazon
driver.get("https://www.amazon.es/s?k=9788418928949")

# Espera a que la página cargue
time.sleep(5)

# Clickamos al botón para aceptar las cookies
driver.find_element(By.XPATH, "//*[@id='sp-cc-accept']").click()

# Espera a que se vea todo
time.sleep(5)

# Agafem el href del llibre
enlace_producto = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")[0].get_attribute('href')

# Obtenemos el precio
precio_producto = driver.find_elements(By.XPATH, "//span[@class='a-offscreen']")[0].get_attribute('innerHTML').replace("&nbsp;", "")
print(f'El enlace del producto es: {enlace_producto}')
print(f'El precio del producto és: {precio_producto}')

# Cerramos el navegador
driver.quit()