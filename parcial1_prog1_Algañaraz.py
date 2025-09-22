titulos = []
ejemplares = []

while True:
    print("\nBienvenidos al menú de la biblioteca.")
    print("Opción 1: Ingresar títulos.")
    print("Opción 2: Ingresar ejemplares.")
    print("Opción 3: Mostrar catálogo.")
    print("Opción 4: Consultar disponibilidad.")
    print("Opción 5: Listar agotados.")
    print("Opción 6: Agregar título.")
    print("Opción 7: Actualizar ejemplares.")
    print("Opción 8: Salir.")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        cantidad_titulos = int(input("Cuántos ejemplares desea ingresar?: "))

        for i in range(cantidad_titulos):
            titulo = input(f"Ingrese el título del libro {i+1}: ").capitalize()

            while titulo in titulos:
                print("Éste libro ya está ingresado.")
                titulo = input(f"Ingrese el título del libro {i+1}: ").capitalize()

            ejemplares.append(0)
            titulos.append(titulo)

        print("Libros ingresados correctamente")

    elif opcion == 2:
        if not titulos:
            print("Primero debe ingresar al menos un libro. (Opción 1).")
        else:
            for i in range(len(titulos)):
                ejemplar = -1

                while ejemplar < 0:
                    ejemplar = int(input(f"Cantidad de ejemplares del '{titulos[i]}': "))

                    if ejemplar < 0:
                        print("No puede ingresar una cantidad negativa.")

                ejemplares[i] = ejemplar

            print("Ejemplares ingresados correctamente.")

    elif opcion == 3:
        if not titulos:
            print("No hay títulos para mostrar.")
        else:
            for i in range(len(titulos)):
                print(f"'{titulos[i]}': {ejemplares[i]} ejemplares disponibles.")

    elif opcion == 4:
        if not titulos:
            print("No hay títulos ingresados para buscar.")
        else:
            titulo_a_buscar = input("Ingrese el nombre del título que desea consultar: ").capitalize()

            if titulo_a_buscar not in titulos:
                print("Éste título no ha sido ingresado.")
            else:
                indice = titulos.index(titulo_a_buscar)
                print(f"El título '{titulos[indice]}' tiene {ejemplares[indice]} ejemplares disponibles.")

    elif opcion == 5:
        if not titulos:
            print("No hay libros ingresados.")
        else:
            agotados = []

            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    agotados.append(titulos[i])

            if agotados:
                for titulo in agotados:
                    print(f"- {titulo}")
            else:
                print("Todos los títulos tienen ejemplares disponibles.")

    elif opcion == 6:
        titulo_a_ingresar = input("Ingrese el nombre del título: ").capitalize()

        if titulo_a_ingresar in titulos:
            print("Éste libro ya ha sido ingresado.")
        else:
            ejemplar = -1

            while ejemplar < 0:
                ejemplar = int(input("Cuántos ejemplares disponibles tiene?: "))
                if ejemplar < 0:
                    print("No puede ingresar una cantidad negativa.")

            ejemplares.append(ejemplar)
            titulos.append(titulo_a_ingresar)
            print("Título ingresado correctamente.")

    elif opcion == 7:
        if not titulos:
            print("Primero debe ingresar títulos.")
        else:
            movimiento = input("Pulse 'p' si desea prestar un libro o 'd' si desea devolverlo: ").lower()

            if movimiento == "d":
                libro_a_devolver = input("Ingrese el nombre del libro que desea devolver: ").capitalize()

                if libro_a_devolver not in titulos:
                    print("Éste libro no ha sido ingresado al sistema.")
                else:
                    indice = titulos.index(libro_a_devolver) 
                    ejemplares[indice] += 1
                    print(f"Devolución realizada con éxito. Quedan {ejemplares[indice]} ejemplares disponibles de '{titulos[indice]}'")

            elif movimiento == "p":
                libro_a_prestar = input("Ingrese el nombre del libro que va a prestar: ").capitalize()

                if libro_a_prestar not in titulos:
                    print("Éste título no ha sido ingresado en el sistema.")
                else:
                    indice = titulos.index(libro_a_prestar)
                    if ejemplares[indice] == 0:
                        print("Éste libro no tiene copias disponibles para prestar.")
                    else:
                        ejemplares[indice] -= 1
                        print(f"Préstamo realizado con éxito. Quedan {ejemplares[indice]} ejemplares disponibles de '{titulos[indice]}'.")

            else:
                print("Opción inválida.")

    elif opcion == 8:
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")