titulos = []
ejemplares = []

while True:
    print("\nBienvenido a la gestión de catálogo de libros.")
    opcion = int(input("Opción 1: Ingresar lista de títulos. \nOpción 2: Ingresar lista de ejemplares disponibles. \nOpción 3: Mostrar catálogo con stock \nOpción 4: Consultar disponibilidad de título disponible \nOpción 5: Listar agotados \nOpción 6: Agregar título \nOpción 7: Actualizar ejemplares (préstamo/devolución) \nOpción 8: Ver catálogo. \nOpción 9: Salir \nElija una opción: "))

    if opcion == 1:
        n = int(input("Cuántos títulos quiere ingresar: "))
        for i in range(n):
            titulo = (input(f"Ingrese el nombre del libro {i+1}: "))
            titulos.append(titulo)
            ejemplares.append(0)

    elif opcion == 2: 
        if not titulos:
            print("Primero ingrese los títulos (opción 1)")
        else: 
            for i in range (len(titulos)):
                ejemplares[i] = input(f"Ingrese la cantidad de ejemplares para '{titulos[i]}': ")
                
    elif opcion == 3:
        if not titulos:
            print("Catálogo vacío.")
        else: 
            for i in range (len(titulos)):
                print(f"{titulos[i]}: {ejemplares[i]} copias")

    elif opcion == 4:
        if not titulos:
            print("Catálogo vacío.")
        else: 
            buscar = input("Ingrese el título a buscar: ")
            if buscar in titulos: 
                indice = titulos.index(buscar)
                print(f"'{buscar}' {ejemplares[indice]} copias disponibles.")
            else: 
                print("Título no disponible.")

    elif opcion == 5: 
        agotados = []
        for i in range (len(titulos)):
            if ejemplares[i] == 0:
                agotados += [titulos[i]]

            if agotados:
                print("\nLibros agotados: ")
                for titulo in agotados:
                    print("-",titulo)
            else:
                print("Todos los libros tienen copias disponibles.")

    elif opcion == 6:
        nuevo_titulo = input("Ingrese el nuevo título: ")
        if nuevo_titulo in titulos:
            print("Este título ya está ingresado.")
        else:
            copias = int(input(f"Ingrese la cantidad de copias para '{nuevo_titulo}': "))
            titulos.append(nuevo_titulo)
            ejemplares.append(copias)
            print("Título ingresado correctamente")

    elif opcion == 7:
        if not titulos:
            print("Catálogo vacío.")
        else: 
            movimiento = input("Desea prestar (p) o devolver (d) un libro?")
            titulo_a_buscar = input("Ingrese el nombre del libro: ")
            indice = titulos.index(titulo_a_buscar)

            if movimiento == "p":
                if titulo_a_buscar in titulos:
                    if ejemplares[indice] == 0:
                        print("Este libro no se puede prestar")
                    else:
                        ejemplares[indice] -= 1
                else:
                    print("Éste libro no se encuentra disponible")

            else:
                if titulo_a_buscar in titulos:
                    ejemplares[indice] += 1
                else: 
                    print("Éste libro no se encuentra disponible.")

#Mostrar solo con stock disponible
    elif opcion == 8:
        if not titulos:
            print("Catálogo vacío.")
        else:
            print("\n Catálogo completo:")
            for titulo in titulos:
                print("-", titulo)

    elif opcion == 9: 
        print("Saliendo del sistema...")
        break