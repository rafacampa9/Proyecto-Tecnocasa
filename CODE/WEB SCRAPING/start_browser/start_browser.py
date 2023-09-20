#driver de selenium
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

#para modificar las opciones de webdriver en Chrome
from selenium.webdriver.chrome.options import Options

#para instalar automáticamente chromedriver
import os
os.environ['WDM_LOCAL'] = '1'
from webdriver_manager.chrome import ChromeDriverManager


from constantes.constantes import USER_AGENT












def start_browser():
    """Inicia Chrome con los parámetros indicados y devuelve el driver"""
    
    path = ChromeDriverManager().install()

    #OPCIONES de CHROME:
    options = Options()
    user_agent = USER_AGENT
    options.add_argument(f'user-agent={user_agent}') #define un user-agent personalizado
    #options.add_argument('--window-size=1000,1000') #configuramos el ancho y largo de la ventana
    options.add_argument('--start-maximized')  #para que la ventana de Chrome aparezca maximizada
    #options.add_argument('--headless') #no se ve abrir la página
    options.add_argument('--disable-web-security') #deshabilita la política del mismo origen o Same Origin Policy
    options.add_argument('--disable-extensions') #para que no cargue las extensiones de Chrome
    options.add_argument('--disable-notifications') #bloquea las notificiaciones de Chrome
    options.add_argument('--ignore-certificate-errors') #para ignorar el aviso "Su conexión es privada"
    options.add_argument('--no-sandbox') #deshabilita el modo sandbox
    options.add_argument('--log-level=3') #para que chromedriver no muestre nada en la terminal
    options.add_argument('--allow-running-insecure-content') #desactiva el aviso de "contenido no seguro"
    options.add_argument('--no-default-browser-check') #evita el aviso de que Chrome no es el navegador por defecto
    options.add_argument('--no-first-run') #evita la ejecución de ciertas tareas que se realizan la primera vez que se ejecuta Chrome
    options.add_argument('--no-proxy-server') #para no usar proxy, sino conexiones directas
    options.add_argument('--disable-blink-features-AutomationControlled') #para desactivar ciertas características que están diseñadas para detectar la automatización a través de herramientas como Selenium
    options.add_argument('--enable-logging')
    options.add_argument('--incognito')
    #options.add_argument('--private')


    #instanciamos el servicio de chromedriver
    s = Service(
        path
        )

    #instanciamos webdriver de selenium con Chrome
    driver = webdriver.Chrome(service=s, options=options) #añadimos el argumento options

    #devolvemos el driver
    return driver

