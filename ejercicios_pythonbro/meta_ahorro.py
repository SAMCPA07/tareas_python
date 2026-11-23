#programa para ahorrar 10000
META_AHORRO = 10000
meta_actual = 0
ahorro_ingresado = 0
cantidad_depositos = 0

print("*******************************************")
print("*** Bienvenido al programa de ahorro ***")
nombre = str(input("Ingresa tu nombre para continuar: " ))
print(f"Bienvenido {nombre} tu ahorro actual es: ${meta_actual}")
print("******************************************* \n")

while meta_actual < META_AHORRO:
    cantidad_depositos += 1
    ahorro_ingresado = float(input("Introduce el monto a ahorrar: "))
    meta_actual += ahorro_ingresado

    if meta_actual <= 0:
        print("No puedes depositar un monto negativo")
        continue
    else:
        print("************************************")
        print("¡Monto depositado correctamente!")
        print(f"Tu ahorro actual es: ${meta_actual}")
        print(f"Has depositado {cantidad_depositos} veces")
        print("************************************")

        if meta_actual >= META_AHORRO:
            print(f"Felicidades {nombre} has alcanzado la meta de ahorro de ${META_AHORRO}")
            print("************************************")
            break
        else:
            print(f"Faltan ${META_AHORRO - meta_actual} para alcanzar la meta")
            print("************************************")
            continue