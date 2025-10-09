def es_palindromo(palabra):
    # Limpiamos la palabra: quitamos espacios y la convertimos en minúsculas.abs
    palabra = palabra.replace(" "," ").lower()
    # Comparamos la palabra con su reverso
    return palabra == palabra[::-1]
while True:
    # Solicitar entrada del usuario
    entrada = input("Ingresa la palabra o frase: ")
    #Verificar si es palíndromo
    if es_palindromo(entrada):
        print("¡Es un palíndromo!")
    else:
        print("No es un palíndromo")