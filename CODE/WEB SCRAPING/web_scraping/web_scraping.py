from selenium.webdriver.support.ui import WebDriverWait

#para condiciones en selenium
from selenium.webdriver.support import expected_conditions as ec

#excepción de timeout en selenium
from selenium.common.exceptions import TimeoutException

#para definir que tipo de búsqueda voy a definir para el elemento
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as bs

from start_browser.start_browser import start_browser

from math import ceil

from time import sleep

from random import randint

from constantes.constantes import CLEANUP














browser = start_browser()
wait = WebDriverWait(browser, 10)




########################################## MENÚ #################################################################

def tecnocasa(province, ccaa, town=''):
    
    province = CLEANUP(province)
    ccaa = CLEANUP(ccaa)
    if town != '':
        town = CLEANUP(town)

    pages = 1
    x = 1
    urls = []
    while x <=pages:
        if x > 1:
            if town == '':
                 browser.get(
                    f'https://www.tecnocasa.es/venta/inmuebles/{ccaa.lower()}/{province.lower()}.html/pag-{x}'
                )

            else:
                browser.get(
                    f'https://www.tecnocasa.es/venta/inmuebles/{ccaa.lower()}/{province.lower()}/{town.lower()}.html/pag-{x}'
                )

            html = browser.page_source
            soup = bs(html, 'lxml')
        else:
            if town == '':
                browser.get(
                    f'https://www.tecnocasa.es/venta/inmuebles/{ccaa.lower()}/{province.lower()}.html'
                )
            else:
                browser.get(
                    f'https://www.tecnocasa.es/venta/inmuebles/{ccaa.lower()}/{province.lower()}/{town.lower()}.html'
                )
            
            try:
                wait.until(
                    ec.element_to_be_clickable(
                        (
                            By.XPATH,
                            '//button[contains(text(), "Aceptar todo")]'
                        )
                    )
                ).click()
            except TimeoutException:
                print('Cookies no aceptadas')
            html = browser.page_source
            soup = bs(html, 'lxml')

            pages = ceil(float(soup.find('h2').find('strong').text)/15)

        elements = soup.find_all('div', {'class': 'estate-card'})
        for element in elements:
            urls.append(element.find('a', {'href': True}).get('href'))
        
        x += 1
        
    print(len(urls))
    properties = [scrapeo_vivienda(url) for url in urls]
    browser.quit()
    
    
    return properties








############################ VIVIENDA #################################################################



def scrapeo_vivienda(url):
    browser.get(
        url
    )
    sleep(randint(3, 5))
    html = browser.page_source
    soup = bs(html, 'lxml')

    labels = []
    values = []

    title = soup.find('h1', {'class' : 'estate-title'})
    if title:
        title = title.text.strip()
        labels.append('title')
        values.append(title)

    price = soup.find('span', {'class' : 'current-price'})
    if price:
        price = int(price.text.split()[0].replace('.', '').strip())
        labels.append('price')
        values.append(price)

    location = soup.find('h2', {'class' : 'estate-subtitle'})
    if location:
        location = location.text.strip()
        labels.append('location')
        values.append(location)

    
    
    r = soup.find('div', {'class' : 'estate-card-data-element estate-card-rooms'})
    s = soup.find('div', {'class' : 'estate-card-data-element estate-card-surface'})
    b = soup.find('div', {'class' : 'estate-card-data-element estate-card-bathrooms'})

    if r:
        rooms = int(r.find('span').text.split()[0].strip())
        labels.append('rooms')
        values.append(rooms)
    if s:
        surface = int(s.find('span').text.split()[0].strip())
        labels.append('surface')
        values.append(surface)
    if b:
        bathrooms = int(b.find('span').text.split()[0].strip())
        labels.append('bathrooms')
        values.append(bathrooms)

    labels_features = []
    values_features = []
    f = soup.find('div', {'class' : 'col-md-12 estate-features'})
    
    if f:
        features = f.find_all('div', {'class' : 'row'})[1:]
        labels_features = [feature.find('div', {'class' : 'col estate-features-title'}).text.strip() for feature in features]
        values_features = [feature.find('div', {'class' : 'col estate-features-value'}).text.strip() for feature in features]
        
    
    vivienda = {}
    vivienda = dict(zip(labels + labels_features, values + values_features))
    

    return vivienda