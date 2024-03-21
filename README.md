# Web Scraping y Actualización de Precios de Libros

Este script en Python está diseñado para obtener información de precios de libros de la librería en línea "Llar del Llibre" y luego actualizar estos datos a través de una API a una aplicación Laravel. Utiliza la biblioteca Selenium para realizar el web scraping y la biblioteca Requests para enviar datos a la API.

## Requisitos

- Python 3.x
- Selenium
- WebDriver (en este caso se utiliza Firefox)
- Requests

## Instalación de Dependencias

```bash
pip install selenium requests
```

## Configuración del Código

1. Asegúrate de tener el navegador Firefox instalado en tu sistema.
2. Cambia la variable `page` al valor correspondiente ("agapea" o "llardelllibre") según la librería en línea que desees obtener los datos.
3. Si es necesario, ajusta el tiempo de espera (`time.sleep()`) según la velocidad de carga de la página.
4. Verifica que la URL de la API en la función `upload_data_api()` sea la correcta.

## Uso

Ejecuta el script proporcionando un ISBN específico como argumento:

```bash
python script.py
```

## Funcionamiento

1. El script accede al sitio web de "Llar del Llibre" o "Agapea" según la configuración.
2. Busca el libro utilizando el ISBN proporcionado.
3. Extrae el nombre del libro, su precio, el ISBN13 y la disponibilidad.
4. Utiliza una API para actualizar la información de precios del libro en una aplicación Laravel.

## Notas

- Este script está diseñado para uso educativo o personal. Asegúrate de cumplir con los términos de servicio del sitio web desde el que estás extrayendo datos.
- Ten en cuenta que el web scraping puede ser bloqueado por los sitios web si se realiza en grandes cantidades o de manera agresiva.

---

Este README proporciona una visión general del funcionamiento y la configuración del script. Si tienes alguna pregunta o necesitas más detalles, no dudes en preguntar.
