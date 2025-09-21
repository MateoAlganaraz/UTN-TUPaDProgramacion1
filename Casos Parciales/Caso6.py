shows = []
entradas = []

while True:
    print("\nBienvenido al menú de shows.")
    print("Opción 1: Registrar los shows programados.")
    print("Opción 2: Definir la cantidad de entradas para cada show.")
    print("Opción 3: Mostrar las entradas disponibles para cada show.")
    print("Opción 4: Consultar entradas de un show.")
    print("Opción 5: Listar shows agotados.")
    print("Opción 6: Agregar show.")
    print("Opción 7: Actualizar entradas (vender/devolver).")
    print("Opción 8: Ver los shows disponibles.")
    print("Opción 9: Salir.")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        cantidad_shows = int(input("Ingrese la cantidad de shows que desea ingresar: "))

        for i in range(cantidad_shows):
            show = input(f"Ingrese el nombre del show {i+1}: ").capitalize()

            while show in shows:
                print("Éste show ya está ingresado.")
                show = input(f"Ingrese el nombre del show {i+1}: ").capitalize()

            shows.append(show)
            entradas.append(0)

    elif opcion == 2:
        if not shows: 
            print("Primero ingrese un show. (Opción 1).")
        else: 
            for i in range(len(shows)):
                entrada = -1 

                while entrada < 0:
                    entrada = int(input(f"Ingrese la cantidad de entradas para '{shows[i]}': "))

                    if entrada < 0:
                        print("No puede ingresar una cantidad de entradas negativa.")

                entradas[i] = entrada

    elif opcion == 3:
        if not shows:
            print("No hay shows para mostrar.")
        else:
            for i in range(len(shows)):
                print(f"{shows[i]}: {entradas[i]} entradas.")

    elif opcion == 4:
        if not shows:
            print("No hay shows disponibles para consultar entradas.")
        else:
            show_a_buscar = input("Ingrese el nombre del show que quiere buscar: ").capitalize()
            if show_a_buscar not in shows:
                print("El título ingresado no está registrado.")
            else:
                indice = shows.index(show_a_buscar)

                print(f"'{shows[indice]}' tiene {entradas[indice]} entradas disponibles")

    elif opcion == 5:
        if not shows:
            print("Primero ingrese shows.")
        else:
            agotados = []

            for i in range(len(shows)):
                if entradas[i] == 0:
                    agotados.append(shows[i])
                
            if agotados:
                for show in agotados:
                    print(f"- {show}")

            else:
                print("Todos los shows tienen entradas disponibles.")

    elif opcion == 6:
        show_a_agregar = input("Ingrese el título del show que quiere agregar: ").capitalize()
        if show_a_agregar in shows:
            print("Éste título ya está ingresado.")
        else:
            shows.append(show_a_agregar)
            entrada = -1 

            while entrada < 0:
                entrada = int(input(f"Ingrese la cantidad de entradas para '{show_a_agregar}': "))

                if entrada < 0:
                    print("No puede ingresar una cantidad de entradas negativa.")

            entradas.append(entrada)

    elif opcion == 7:
        if not shows:
            print("Primero ingrese shows.")
        else:
            movimiento = input("Pulse 'v' para vender o 'd' para devolución: ").lower()

            if movimiento == "d":
                show_a_devolver = input("De qué show desea devolver las entradas?: ").capitalize()
                if show_a_devolver not in shows:
                    print("Éste show no ha sido ingresado.")
                else:
                    cantidad = -1

                    while cantidad < 0:
                        cantidad = int(input("Cuántas entradas desea devolver?: "))
                        if cantidad < 1:
                            print("Debe devolver al menos una entrada.")

                    indice = shows.index(show_a_devolver)
                    entradas[indice] += cantidad
                    print(f"Devolución realizada con éxito. Quedan {entradas[indice]} entradas disponibles")

            elif movimiento == "v":
                show_a_vender = input("De qué show desea vender las entradas?: ").capitalize()
                if show_a_vender not in shows:
                    print("Éste show no ha sido ingresado.")
                else:
                    cantidad = -1

                    while cantidad < 0:
                        cantidad = int(input("Cuántas entradas desea vender?: "))
                        if cantidad < 0:
                            print("No puede vender una cantidad negativa.")
                    
                    indice = shows.index(show_a_vender)
                    if cantidad > entradas[indice]:
                        print("No tiene esas suficientes entradas para vender.")
                    else:
                        entradas[indice] -= cantidad
                        print(f"Venta registrada con éxito. Quedan {entradas[indice]} entradas disponibles.")

    elif opcion == 8:
        if not shows:
            print("No hay shows ingresados para mostrar.")
        else:
            shows_a_mostrar = []
            for i in range(len(shows)):
                if entradas[i] > 0:
                    shows_a_mostrar.append(shows[i])
                
            if shows_a_mostrar:
                for show in shows_a_mostrar:
                    print(f"- {show}")

            else:
                print("Todos los shows están agotados.")

    elif opcion == 9:
        print("Saliendo del sistema...")
        break











                    
            


        

