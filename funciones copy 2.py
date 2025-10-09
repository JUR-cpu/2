opcion_uno = ["Edgay"]
opcion_dos = ["Jorge"]
opcion_tres = ["Camila"]
opcion_cuatro = ["Bruno"]
opcion_cinco = ["Lau"]
registro = input("Ingresa tu nombre: ")

if registro.lower() == opcion_uno:
    print("¡Hola!", registro ," Bienvenido, ¿listo para empezar?")
    entrada = input("Si/No: ")
    if entrada == "Si":
        programa = input("Ingresa el programa")
