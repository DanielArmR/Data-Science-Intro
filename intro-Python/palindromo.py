def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def main():
    palabra = input('Escribe una palabara: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')
##Buena practica dejar dos espacios entre funciones
##Punto de entrada en un programa de python
if __name__ == '__main__':
    main()