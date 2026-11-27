# EQUIPO 
# 1. CASANOVA PANTOJA JESUS SANTIAGO
# 2. SALINAS MEZA EMANUELL
# 3. May Arcos Josue Matias

import datetime  #se importa la librería datetime para poder mostrar la fecha y hora en el ticket

NIP = 1234 # se define el NIP correcto del usuario
saldo_actual = 1000  # saldo inicial del usuario

# funcion principal que se ejecuta al iniciar el programa
def main():
    print("Bienvenido al cajero automático")
    for i in range(3): # bucle que permite al usuario ingresar su NIP hasta 3 veces
        try:
            nip_ingresado = int(input("Ingrese su NIP: "))
        except ValueError: # si el usuario ingresa un valor que no es un número entero, se le pedirá que ingrese un número válido
            print("Por favor, ingrese un número válido")
            continue # continúa con la siguiente vuelta del bucle

        if nip_ingresado == NIP: # si el NIP ingresado es correcto, se le da la bienvenida al usuario y se le muestra el menú principal
            print("NIP correcto, ¡Bienvenido al cajero automático!")
            while True:
                opcion = menu_principal() # se manda a llamar la función menu_principal para que el usuario seleccione una opción

                # dependiendo que opcion retorne la función menu_principal, se ejecutará la función correspondiente
                if opcion == 1:
                    consultar_saldo() # Solo consulta el saldo, no imprime ticket porque no modifica el saldo
                elif opcion == 2:
                    operacion, monto = depositar()
                    if monto > 0:  # Solo imprime ticket si el depósito fue válido
                        ticket(operacion, monto, saldo_actual)
                elif opcion == 3:
                    operacion, monto = retirar()
                    if monto > 0:  # Solo imprime ticket si el retiro fue exitoso
                        ticket(operacion, monto, saldo_actual)
                elif opcion == 4:
                    operacion, monto = transferir()
                    if monto > 0:  # Solo imprime ticket si la transferencia fue válida
                        ticket(operacion, monto, saldo_actual)
                elif opcion == 5:
                    pagar_servicios() # El submenú gestiona internamente cada servicio y su ticket
                elif opcion == 6:
                    print("Gracias por usar el cajero. ¡Hasta luego!")
                    break
                else:
                    print("Opción no válida.") # si el usuario ingresa una opción que no está en el menú, se le informará que la opción no es válida
            return
        else:
            print("NIP incorrecto, intente de nuevo")
            
    print("Ha excedido el número máximo de intentos. Tarjeta bloqueada.") # bloqueo de tarjeta al exceder 3 intentos de NIP incorrectos

# FUNCIONES DEL ATM
# Cada función corresponde a una operación del cajero automático,
# como consultar saldo, depositar, retirar, transferir y pagar servicios. 
# Cada función maneja la lógica de la operación y retorna información relevante 
# para imprimir un ticket si es necesario.
# TODAS LAS FUNCIONES RETORNAN 2 VALORES (excepto, consultar saldo)
# EN TODAS LA FUNCIONES SE INCLUYE VALIDACION DE ENTRADAS (para evitar errores de tipo y valores negativos)
# SE RETORNA EL TIPO DE OPERACION REALIZADA (en otras palabras, el nombre de la funcion)
# EN CASO DE SER EXITOSA, SE RETORNA EL MONTO DE LA OPERACION, EN CASO CONTRARIO SE RETORNA 0
# EN CASO DE SER EXITOSA, SE IMPRIME EL TICKET CON LA FUNCION "ticket" 
# QUE RECIBE 3 PARAMETROS: TIPO DE OPERACION, MONTO (solo si corresponde) Y SALDO ACTUAL




# funcion de menu principal
# muestra las opciones disponibles para el usuario y retorna la opción seleccionada
# si el usuario ingresa una opcion invalida, retorna 0 para que se valide "opcion no valida"
def menu_principal():
    print("\nBienvenido a este ATM, seleccione una opción:")
    print("1. Consultar Saldo\n"
          "2. Depositar saldo\n"
          "3. Retirar efectivo\n"
          "4. Transferir\n"
          "5. Pagar servicios\n"
          "6. Salir")
    try: # se intenta convertir la entrada del usuario a un número entero
        return int(input("Seleccione una opción: "))
    except ValueError: # retorna 0 si se ingresa una opcion invalida
        return 0  # Retorna 0 para que caiga en "Opción no válida"



# funcion para consultar saldo, solo muestra el saldo del cliente
def consultar_saldo():
    print(f"Su saldo actual es: ${saldo_actual:.2f}")


# funcion para depositar
def depositar():
    global saldo_actual # se llama la variable global saldo actual
    try: # se intenta convertir la variable a depositar a float
        monto = float(input("Ingrese el monto a depositar: "))
        if monto > 0: # si el monto es mayor a cero, retorna el valor de deposito 
            saldo_actual += monto
            return "Depósito", monto # retorna el valor depositado
        else:
            print("El monto debe ser mayor a 0.")
            return "Depósito", 0 # se cancela la funcion si el deposito es 0 
    except ValueError: 
        print("Monto inválido.") # si el monto es invalido, de igual forma, se cancela
        return "Depósito", 0


# funcion "retirar"
def retirar():
    global saldo_actual # se manda a llamar la variable global "saldo_actual" para continuar la funcion
    try:
        monto = float(input("Ingrese el monto a retirar: ")) # se le pide al usuario el monto
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
            return "Retiro", 0 # se cancela la funcion si el usuario ingresa un monto menor o igual a 0 y se retorna
        elif monto > saldo_actual:
            print("Saldo insuficiente.") # validacion para el saldo
            return "Retiro", 0
        else:
            saldo_actual -= monto 
            return "Retiro de efectivo", monto # se concreta la funcion si el deposito y el saldo actual son validados
    except ValueError:
        print("Monto inválido.")
        return "Retiro", 0 # se valida entradas invalidas y se cancela la funcion retornando 0


# funcion transferir
def transferir():
    global saldo_actual # se manda a llamar la variable global "saldo_actual"
    cuenta_destino = input("Ingrese el número o identificador de la cuenta destino: ").strip() # el .strip() elimina espacios en blanco al inicio y al final de la cadena
    if cuenta_destino == "": # se valida la cuenta destino, si esta vacia, se cancela la funcion y se retorna 0
        print("La cuenta destino no puede estar vacía.") 
        return "Transferencia", 0

    # se valida el monto a transferir, si es mayor a 0 y menor o igual al saldo actual, se concreta la transferencia
    try:
        monto = float(input("Ingrese el monto a transferir: ")) # se pide el monto a transferir y se convierte a float
        if monto <= 0: # se valida que el monto sea mayor a 0, si no lo es, se cancela la funcion y se retorna 0
            print("El monto debe ser mayor a 0.") 
            return "Transferencia", 0
        elif monto > saldo_actual: # si hay fondos insuficientes, se cancela la funcion y se retorna 0
            print("Saldo insuficiente para realizar la transferencia.")
            return "Transferencia", 0
        else: # si el saldo es suficiente, se concreta la transferencia y se retorna el tipo de operacion y el monto transferido
            saldo_actual -= monto
            print(f"Transferencia exitosa a la cuenta {cuenta_destino}.")
            return f"Transferencia (Cuenta: {cuenta_destino})", monto
    except ValueError: # se ingresa un valor que no es un número, se cancela la funcion y se retorna 0
        print("Monto inválido.")
        return "Transferencia", 0


# funcion pagar servicios
def pagar_servicios():
    global saldo_actual # se manda a llamar la variable global "saldo_actual" para continuar la funcion
    while True: # mientras sea verdadero, se ejecuta el bucle para que el usuario pueda pagar servicios hasta que decida regresar al menu principal
        print("\n--- PAGO DE SERVICIOS ---") # se muestra el menu de servicios disponibles para pagar
        print("1. Pago de luz\n"
              "2. Pago de agua\n"
              "3. Recarga de saldo celular\n"
              "4. Regresar al menú principal")
        # se valida la opcion ingresada por el usuario, 
        # si es un valor que no es un número entero, se le pedirá que ingrese una opción válida
        try:
            opcion_servicio = int(input("Seleccione un servicio: "))
        except ValueError:
            print("Por favor, ingrese una opción válida.")
            continue

        # dependiendo de la opción seleccionada, se ejecutará la función correspondiente para pagar el servicio 
        if opcion_servicio == 1: # pago de luz
            num_servicio = input("Ingrese el número de servicio de luz (CFE): ").strip()
            if num_servicio == "":
                print("Número de servicio inválido.")
                continue
            try: # se valida el monto a pagar, si es mayor a 0 y menor o igual al saldo actual, se concreta el pago del servicio
                monto = float(input("Ingrese el monto a pagar del recibo de luz: "))
                if monto <= 0: # validacion de monto, si es menor o igual a 0, se cancela la funcion y se retorna 0
                    print("El monto debe ser mayor a 0.")
                elif monto > saldo_actual:
                    print("Saldo insuficiente para pagar el servicio de luz.")
                else:
                    saldo_actual -= monto
                    ticket(f"Pago de luz (Ref: {num_servicio})", monto, saldo_actual)
            except ValueError:
                print("Monto inválido.")

        elif opcion_servicio == 2: # pago de agua
            # mismo procedimieto que el pago de luz, se valida el número de contrato y el monto a pagar
            num_cuenta = input("Ingrese el número de contrato de agua: ").strip()
            if num_cuenta == "":
                print("Número de contrato inválido.")
                continue
            try:
                monto = float(input("Ingrese el monto a pagar del recibo de agua: "))
                if monto <= 0:
                    print("El monto debe ser mayor a 0.")
                elif monto > saldo_actual:
                    print("Saldo insuficiente para pagar el servicio de agua.")
                else:
                    saldo_actual -= monto
                    ticket(f"Pago de agua (Contrato: {num_cuenta})", monto, saldo_actual)
            except ValueError:
                print("Monto inválido.")

        elif opcion_servicio == 3: # recarga de saldo celular
            #mismo procedimiento que el pago de luz y agua, se valida el número celular, la compañía y el monto a recargar
            numero_cel = input("Ingrese el número celular a 10 dígitos: ").strip()
            if len(numero_cel) != 10 or not numero_cel.isdigit():
                print("Número inválido. Debe contener exactamente 10 dígitos numéricos.")
                continue
            compania = input("Ingrese la compañía telefónica: ").strip()
            if compania == "":
                print("Debe especificar una compañía.")
                continue
            try:
                monto = float(input("Ingrese el monto de la recarga: "))
                if monto <= 0:
                    print("El monto debe ser mayor a 0.")
                elif monto > saldo_actual:
                    print("Saldo insuficiente para realizar la recarga.")
                else:
                    saldo_actual -= monto
                    ticket(f"Recarga celular ({compania} - {numero_cel})", monto, saldo_actual)
            except ValueError:
                print("Monto inválido.")

        elif opcion_servicio == 4: # regresar al menú principal
            print("Regresando al menú principal...")
            break
        else:
            print("Opción no válida.")



# FUNCION TICKET 
# en cada funcion, se retorna el tipo de operacion y el monto, si la operacion fue exitosa, se manda a llamar la funcion ticket
# dependiendo si la operacion fue exitosa o no, se imprimira el ticket con la informacion correspondiente
# se imprime el tipo de operacion, el monto (si corresponde) y el saldo actual, junto con la fecha y hora de la transaccion
# la fecha se obtiene con la libreria datetime y se formatea para mostrarla en el ticket
# se redondea a dos decimales el monto y el saldo actual para que se vea mas presentable en el ticket
def ticket(tipo_operacion, monto, saldo):
    fecha = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")  # se obtiene la fecha y hora actual
    print("\nImprimiendo ticket...")
    print("***************************")
    print("*         TICKET          *")
    print("Operación:", tipo_operacion)
    print(f"Monto: ${monto:.2f}")
    print(f"Saldo actual: ${saldo:.2f}")
    print("Fecha y hora:", fecha)
    print("***************************")


main()
