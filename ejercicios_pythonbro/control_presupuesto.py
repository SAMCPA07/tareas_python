print("Control de presupuesto del evento")

total_gastado = 0.0

cantidad_conceptos = int(input("Ingresa la cantidad de conceptos a revisar: "))

for i in range(cantidad_conceptos):
    print(f"\n--- Concepto {i + 1} ---")

    concepto = input("Ingresa el nombre del concepto: ")
    presupuesto = float(input("Ingresa el presupuesto asignado: "))
    gasto = float(input("Ingresa el gasto realizado: "))

    if gasto <= presupuesto:
        diferencia = presupuesto - gasto
        print(f"El gasto está dentro del presupuesto. Quedaron disponibles: ${diferencia:.2f}")
    else:
        diferencia = gasto - presupuesto
        print(f"El gasto se excedió del presupuesto por: ${diferencia:.2f}")

    total_gastado += gasto

print(f"\nTotal gastado en el evento: ${total_gastado:.2f}")