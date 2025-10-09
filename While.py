import random
numero_secreto = random.randint(1,10)
intentos = 0
print("¡Adivina el número secreto entre 1 y 10!")
while True:
    intento = int(input("Ingresa tu número: "))
    intento += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos")
        break
    elif intento < numero_secreto:
        print("Demasiado bajo, intente de nuevo")
    elif intento > numero_secreto:
        print("Demasiado alto, intenta de nuevo")
