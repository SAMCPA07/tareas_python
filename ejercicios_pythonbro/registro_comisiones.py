TASA_COMISION = 0.05
BONO_EXTRA = 200
META_VENTAS = 5000

total_pagar = 0.0
contador_bonos = 0

print("--- Registro de comisiones ---")
cantidad_vendedores = int(input("Introduce la cantidad de vendedores: "))

for i in range(cantidad_vendedores):
    print(f"\n--- Vendedor {i + 1} ---")
    nombre_vendedor = input("Introduce el nombre del vendedor: ")
    ventas = float(input("Introduce el monto de ventas: "))

    es_valido = ventas >= 0

    if not es_valido:
        print("Registro no válido. El monto no puede ser negativo.")
    else:
        comision = ventas * TASA_COMISION
        pago_individual = comision

        if ventas >= META_VENTAS:
            pago_individual += BONO_EXTRA
            contador_bonos += 1
            print(f"¡Felicidades! Se alcanzó la meta de ventas y obtuviste un bono de ${BONO_EXTRA}")

        print(f"El pago individual para {nombre_vendedor} es: ${pago_individual:.2f}")
        total_pagar += pago_individual

print("\n--- Resumen Final ---")
print(f"El total a pagar por la empresa es: ${total_pagar:.2f}")
print(f"Vendedores que recibieron el bono extra: {contador_bonos}")