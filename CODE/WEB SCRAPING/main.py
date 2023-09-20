from web_scraping.web_scraping import tecnocasa
from constantes.constantes import PATH
import pandas as pd


if __name__=='__main__':
    province = input('Introduzca la provincia: ')
    ccaa = input('Introduzca la comunidad autónoma: ')
    town = input('Introduzca el municipio: ')
    viviendas = tecnocasa(province, ccaa, town)
    df = pd.DataFrame(viviendas)
    print(df)
    df.to_json(PATH)
    
    