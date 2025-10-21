math = float(input("Tu calificación de Matemáticas"))
fisi = float(input("Tu calificación de Física"))
english = float(input("Tu calificación de Inglés"))
promedio = (english+math+fisi)/3
print("Tu promedio es ", promedio)
if promedio ==100:
    print("¡IMPOSIBLE!")
elif promedio > 90:
    print("Excelente")
elif promedio > 80:
    print("Muy bien")
elif promedio > 70:
    print("Aprobaste")
    print("Felicidades")
elif promedio < 70:
    print("Reprobaste")

opcion = int(input("Escribe la opción que desees usar"))
if opcion == 1:
    print("Tu calificación es de ", promedio, "sobre 100")
    opcion_uno = input("Deseas hacer otra operación?")
    if opcion_uno == "si":
        print("Tendrás que regresar al menú principal")
        ejecutar = True
    elif opcion_uno == "no":
        print("Gracias por visitarnos, hasta luego")
        ejecutar= False
    else:
        print("Opción no válida")