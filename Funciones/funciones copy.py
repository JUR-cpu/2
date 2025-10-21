def verificar_numero(n):
    if n>0:
        print("El número es positivo")
    elif n<0:
        print("El número es negativo")
    else:
        print("El número es cero")

while True:
    #solicitar número al usuario
    numero = int(input("Ingresa un número: "))
    verificar_numero (numero)