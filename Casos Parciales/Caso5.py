platos = []
porciones = []

while True:
    print("\nBienvenido al menú del restaurante")
    print("Opción 2: Ingresar porciones disponibles.")
    print("Opción 3: Mostrar platos y sus porciones")
    print("Opción 4: Consultar porciones de un plato.")
    print("Opción 5: Listar platos agotados.")
    print("Opción 6: Agregar plato.")
    print("Opción 7: Vender/Devolver porciones.")
    print("Opción 8: Ver los platos con porciones disponibles.")
    print("Opción 9: Salir")
    opcion = int(print("Elija una opción: "))

    if opcion == 1:
        cantidad_platos = int(input("Cuántos platos desea ingresar?: "))

        for i in range(cantidad_platos):
            plato = input(f"Ingrese el nombre del plato {i+1}: ").lower()
            platos.append(plato)
            porciones.append(0)

        print("Platos ingresado correctamente.")

    elif opcion == 2:
        if not platos:
            print("Primero ingrese un plato. (Opción 1)")
        else:
            for i in range(len(platos)):
                porcion = -1

                while porcion < 0:
                    porcion = int(input(f"Ingrese la cantidad de porciones de '{platos[i]}' que hay disponibles: "))
                    if porcion < 0:
                        print("No se puede ingresar una cantidad negativa.")
                    
                    porciones[i] = porcion

    elif opcion == 3:
        if not platos:
            print("No hay platos para mostrar.")
        else:
            for i in range(len(platos)):
                print(f"- '{platos[i]}' tiene {porciones[i]} porciones disponibles.")

    elif opcion == 4:
        if not platos:
            print("No hay platos para consultar sus porciones.")
        else:
            plato_a_buscar = input("Ingrese el nombre del plato: ").lower()

            if plato_a_buscar not in platos:
                print("Éste plato no se ha ingresado.")
            else:
                indice = platos.index(plato_a_buscar)
                print(f"'{plato_a_buscar}' tiene {porciones[indice]} porciones disponibles.")

    elif opcion == 5:
        if not platos:
            print("No hay platos ingresados.")
        else:
            agotados = []
            for i in range(len(platos)):
                if porciones[i] == 0:
                    print(f"- {platos[i]}")

    elif opcion == 6:
        plato_a_ingresar = input("Ingrese el nombre del plato nuevo: ").lower()
        platos.append(plato_a_ingresar)

        porcion = -1
        while porcion < 0:
            porcion = int(input("Cuántas porciones disponibles tiene?: "))
            if porcion < 0:
                print("No puede ingresar una cantidad negativa.")
            else:
                porciones.append(porcion)
                print("Plato ingresado correctamente.")
        
    elif opcion == 7:
        if not platos:
            print("Primero ingrese un plato.")
        else:

            movimiento = input("Pulse 'v' si desea vender o 'd' si desea devolver: ").lower()

            if movimiento == "d":

                plato_a_devolver = input("Ingrese el nombre del plato que va a devolver: ").lower()

                if plato_a_devolver not in platos:
                    print("Éste plato no se ha ingresado.")
                else:
                    cantidad = -1
                    indice = platos.index(plato_a_devolver)

                    while cantidad < 0 or cantidad > 100:
                        cantidad = int(input("Cuántos platos desea devolver?: "))
                        if cantidad < 0:
                            print("No puede devolver una cantidad negativa.")
                        elif cantidad > 100:
                            print("Por favor ingrese una cantidad real que va a devolver.")
                        
                    porciones[indice] += cantidad
                    print(f"Devolución realizada. Ahora hay {porciones[indice]} porciones de '{plato_a_devolver}'")

            elif movimiento == "v":

                plato_a_vender = input("Ingrese el nombre del plato que quiere vender: ").lower()

                if plato_a_vender not in platos:
                    print("Éste plato no ha sido ingresado.")
                else:
                    cantidad = -1
                    indice = platos.index(plato_a_vender)

                    while cantidad < 0 or cantidad > porciones[indice]:
                        cantidad = int(input("Cuántas porciones quiere vender?: "))
                        if cantidad < 0:
                            print("No puede vender una cantidad negativa.")
                        elif cantidad > porciones[indice]:
                            print("No tiene esa cantidad de porciones para vender.")
                    
                    porciones[indice] -= cantidad
                    print(f"Venta realizada con éxito. Ahora quedan {porciones[indice]} de '{plato_a_vender}'")

            else:
                print("Opción inválida.")

    elif opcion == 8:
        if not platos:
            print("No hay platos disponibles para mostrar.")
        else: 
            platos_a_mostrar = []
            agotados = []
            
            for i in range(len(platos)):
                if porciones[i] > 0:
                    print(f"- {platos[i]}")
                else:
                    agotados.append(platos[i])
                
    elif opcion == 9:
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")