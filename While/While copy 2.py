password = "Hamburguesa con papas"
oportunidad = 3

while oportunidad == 3:
    entrada = input("Ingresa la cntraseña: ")

    if entrada == password:
        print("Acceso concedido")
        break
    else:
        print("Intente de nuevo, intentos restantes:", oportunidad)
        oportunidad -= 1

if oportunidad == 0:
    print("Bloqueado. Acceso denegado")

else:
     print("Acceso concedido")