USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

PATH = 'D:/Escritorio/Ubuntu/Proyecto Tecnocasa/DATA'

def CLEANUP(word):
    if 'á' in word: word = word.replace('á', 'a')
    if 'é' in word: word = word.replace('é', 'e')
    if 'í' in word: word = word.replace('í', 'i')
    if 'ó' in word: word = word.replace('ó', 'o')
    if 'ú' in word: word = word.replace('ú', 'u')
    if 'ü' in word: word = word.replace('ü', 'u')
    if 'ñ' in word: word = word.replace('ñ', 'n')

    lista = []
    for a in word:
        if a == ' ':
            lista.append('-')
        else:
            lista.append(a)

    word = ''.join(lista)

    return word