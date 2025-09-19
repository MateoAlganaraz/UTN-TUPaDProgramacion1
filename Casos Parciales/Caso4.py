clases = []
cupos =[]

while True:
    print("\nBienvenido al menú del gimnasio")
    opcion = int(input("Opción 1: Registrar las clases ofrecidas. \nOpción 2: Definir la capacidad de cada clase. \nOpción 3: Mostrar disponibilidad de cada clase. \nOpción 4: Consultar cupos de una clase. \nOpción 5: Listar clases sin cupos. \nOpción 6: Agregar clase. \nOpción 7: Actualizar cupos (inscribir/baja). \nOpción 8: Ver clases con cupos disponibles. \nOpción 9: Salir. \nElija una opción: "))

    if opcion == 1:
        cantidad_clases = int(input("Cuántas clases desea ingresar?: "))
        for i in range(cantidad_clases):
            clase = input(f"Ingrese el nombre de la clase {i+1}: ")
            clases.append(clase)
            cupos.append(0)
            
        print("Clases agregadas correctamente.")

    elif opcion == 2:
        if not clases:
            print("Primero ingrese las clases. (Opción 1).")
        else: 
            for i in range(len(clases)):
                cupos[i] = int(input(f"Ingrese los cupos disponibles para la clase '{clases[i]}': "))


    elif opcion == 3:
        if not clases:
            print("No hay clases ingresadas para mostrar.")
        else:
            for i in range(len(clases)):
                print(f"'{clases[i]}' tiene {cupos[i]} turnos disponibles.")

    elif opcion == 4:
        if not clases:
            print("Todavía no hay clases ingresadas.")
        else:
            clase_a_buscar = input("Ingrese el nombre de la clase: ")
            if clase_a_buscar not in clases:
                print("Ésta clase no ha sido ingresada todavía.")
            else:
                indice = clases.index(clase_a_buscar)
                print(f"La clase '{clase_a_buscar}' tiene {cupos[indice]} cupos disponibles")

    elif opcion == 5:
        if not clases:
            print("Primero debe ingresar al menos una clase.")
        else:
            clases_llenas = []
            for i in range(len(clases)):
                if cupos[i] == 0:
                    clases_llenas.append(clases[i])

            if clases_llenas:
                for clase in clases_llenas:
                    print(f"- {clase}")
            else:
                print("Todas las clases tienen cupos disponibles.")

    elif opcion == 6:
        clase_a_agregar = input("Ingrese el nombre de la clase que desea agregar: ")

        if clase_a_agregar in clases:
            print("Ésta clase ya está ingresada. ")
        else:
            cupos_clase_nueva = int(input(f"Cuántos cupos disponibles va a tener la clase '{clase_a_agregar}'?: "))

            clases.append(clase_a_agregar)
            cupos.append(cupos_clase_nueva)
            print("Clase agregada correctamente.")

    elif opcion == 7:
        if not clases:
            print("Primero ingrese una clase.")
        else:
            movimiento = input("Pulse 'i' para inscribirse a una clase o 'c' para cancelar su turno: ")
            if movimiento == "i":
                clase_inscribirse = input("A qué clase le gustaría inscribirse?: ")
                if clase_inscribirse not in clases:
                    print("Ésta clase no se encuentra entre las opciones.")
                else: 
                    indice = clases.index(clase_inscribirse)
                    if cupos[indice] == 0:
                        print("No quedan cupos disponibles en ésta clase.")
                    else:
                        cupos[indice] -= 1
                        print("Inscripción realizada con éxito.")
            elif movimiento == "c":
                cancelar_clase = input("De qué clase desea cancelar su turno?: ")
                if cancelar_clase not in clases:
                    print("Ésta clase no se encuentra entre las opciones.")
                else:
                    indice = clases.index(cancelar_clase)
                    cupos[indice] += 1
                    print("Turno cancelado con éxito.")
            else:
                print("Opción inválida.")

    elif opcion == 8:
        if not clases:
            print("No hay clases ingresadas para mostrar.")
        else:
            clases_a_mostrar = [] 
            clases_llenas = []
            for i in range(len(clases)):
                if cupos[i] > 0:
                    clases_a_mostrar.append(clases[i])
                else:
                    clases_llenas.append(clases[i])
            
            #Mostrar nombres clases con turnos disponibles
            for i in range(len(clases_a_mostrar)):
                print("-",clases_a_mostrar[i])

    elif opcion == 9:
        print("Saliendo del sistema...")
        break

    else: 
        print("Opción inválida.")