tarjetas = []
saldos = []

while True:
    print("\nBIENVENIDO AL MENÚ DE SUBE")
    opcion = int(input("Opción 1: Ingresar número tarjeta \nOpción 2: Ingresar saldos correspondientes \nOpción 3: Mostrar todas las tarjetas y saldos \nOpción 4: Consultar saldo por número \nOpción 5: Listar saldos en negativo \nOpción 6: Agregar tarjeta \nOpción 7: Cargar/debitar saldo \nOpción 8: Mostrar tarjetas con saldo positivo \nOpción 9: Salir \nElija una opción: "))

    if opcion == 1:
        n = int(input("Cuántas tarjetas desea ingresar?: "))
        if n < 1:
            continue
        else:
            for i in range(n):
                while True:
                    num_tarjeta = input(f"Ingrese el número de la tarjeta {i+1}: ")

                    if len(num_tarjeta) == 16 and num_tarjeta.isdigit():
                        tarjetas.append(num_tarjeta)
                        saldos.append(0.0)
                        print(f"Tarjeta registrada correctamente")
                        break
                    else:
                        print("Ingreso incorrecto. La tarjeta debe tener 16 dígitos numéricos.")

    if opcion == 2:
        if not tarjetas:
            print("Primero debe ingresar el número de la tarjeta. (Opción1)")
        else: 
            for i in range(len(tarjetas)): 
                saldos[i] = float(input(f"Ingrese el saldo para la tarjeta '{tarjetas[i]}': "))

    if opcion == 3:
        if not tarjetas:
            print("No hay tarjetas para mostrar.")
        else: 
            for i in range(len(tarjetas)):
                print(f"Tarjeta número '{tarjetas[i]}' tiene ${saldos[i]} de saldo disponible")

    if opcion == 4:
        if not tarjetas:
            print("Aún no hay tarjetas registradas.")
        else: 
            tarjeta_a_buscar = input("Ingrese el número de la tarjeta a buscar: ")
            if tarjeta_a_buscar not in tarjetas:
                print("Ésta tarjeta no está registrada.")
            else:
                indice = tarjetas.index(tarjeta_a_buscar)
                print(f"La tarjeta número '{tarjeta_a_buscar}' tiene un saldo disponible de ${saldos[indice]}")

    if opcion == 5:
        if not tarjetas:
            print("No hay tarjetas ingresadas.")
        else:
            saldos_negativos = []
            for i in range(len(tarjetas)):
                if saldos[i] < 1:
                    saldos_negativos.append(tarjetas[i])
            
            if saldos_negativos:
                for plata in saldos_negativos:
                    print("-",plata)
            
            else:
                print("Todas las tarjetas tienen saldo positivo.")

    if opcion == 6:
        tarjeta_nueva = input("Ingrese el número de la tarjeta nueva: ")
        if tarjeta_nueva in tarjetas:
            print("Ésta tarjeta ya está ingresada.")
            continue
        else:
            if len(tarjeta_nueva) == 6 and tarjeta_nueva.isdigit():
                tarjetas.append(tarjeta_nueva)
                saldo_tarjeta_nueva = float(input("Ingrese el saldo de la tarjeta nueva: "))
                saldos.append(saldo_tarjeta_nueva)
                print(f"Tarjeta registrada correctamente")
            else:
                print("Ingreso incorrecto. La tarjeta debe tener 16 dígitos numéricos.")
            
    if opcion == 7:
        if not tarjetas:
            print("Antes debe ingresar una tarjeta.")
        else:
            tarjeta_a_modificar = input("Ingrese el número de la tarjeta: ")

            if tarjeta_a_modificar not in tarjetas:
                print("Ésta tarjeta no ha sido ingresada en el sistema.")
            else:
                movimiento = input("pulse 'c' para cargar o 'd' para debitar: ").lower()
                indice = tarjetas.index(tarjeta_a_modificar)
                
                if movimiento == "c":
                    while True:
                        carga_str = input(f"Cuánto saldo desea cargarle a la tarjeta '{tarjeta_a_modificar}': ")

                        if carga_str.isdigit():
                            carga = float(carga_str)
                            if carga > 0:
                                saldos[indice] += carga
                                print(f"Carga realizada con éxito. Su saldo nuevo es de ${saldos[indice]}.")
                                break
                        else:
                            print("Ingrese sólo números postivos.")

                elif movimiento == "d":
                    
                    while True:

                        debito_str = input(f"Cuándo saldo desea debitar de la tarjeta '{tarjeta_a_modificar}'?: ")

                        if debito_str.isdigit():
                            debito = float(debito_str)
                            if debito <= 0:
                                print("Por favor ingrese un saldo positivo.")
                                continue
                            elif debito > saldos[indice]:
                                print("No puede dejar su tarjeta en negativo.")
                                continue
                            else:
                                saldos[indice] -= debito
                                print(f"Débito hecho con éxito. Su saldo nuevo es de ${saldos[indice]}.")
                                break
                        else:
                            print("Ingrese sólo números")

                else:
                    print("Opción inválida.")

    #Solo muestra las tarjetas con saldos positivos
    if opcion == 8:
        saldos_negativos = []
        if not tarjetas:
            print("No hay tarjetas para mostrar.")
        else: 
            for i in range(len(tarjetas)):
                if saldos[i] < 1:
                    saldos_negativos.append(saldos[i])
                    print("No hay tarjetas con saldo positivo.")
                else:
                    print(f"Tarjeta '{tarjetas[i]}' tiene ${saldos[i]}")

    if opcion == 9:
        print("Saliendo del sistema...")
        break
