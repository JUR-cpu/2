clave_correcta = "dinosaurio"
intentos = 3
while intentos > 0:
    clave=input("Introduce la contraseña ")
    if clave == clave_correcta:
        print("Acceso concedido.")
        break
    else:
        intentos -= 1
        print("Contraseña incorrecta, Intentos restantes ", intentos)
else:
    print("Acceso bloqueado.")