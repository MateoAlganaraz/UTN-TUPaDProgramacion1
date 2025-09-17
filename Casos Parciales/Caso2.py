from datetime import datetime, timedelta

especialidades = []
cupos = []

while True:
    print("\nBienvenido/a al menú de la clínica.")
    opcion = int(input("Opción 1: Ingresar lista de especialidades. \nOpción 2: Ingresar lista de cupos disponibles. \nOpción 3: Mostrar agenda \nOpción 4: Consultar cupos de una especialidad \nOpción 5: Listar especialidades sin cupo \nOpción 6: Agregar especialidad \nOpción 7: Actualizar cupos (reservar/cancelar) \nOpción 8: Ver agenda completa \nOpción 9: Salir \nElija una opción: "))

    if opcion == 1:
        n = int(input("Cuántas especialidades desea ingresar: "))
        for i in range(n):
            especialidad = (input(f"Ingrese el nombre de la especialidad {i+1}: ")).lower()
            especialidades.append(especialidad)
            cupos.append(0)

    if opcion == 2: 
        if not especialidad:
            print("Primero ingrese las especialidades (opción 1)")
        else: 
            for i in range (len(especialidades)):
                cupos[i] = int(input(f"Ingrese la cantidad de cupos disponibles para '{especialidades[i]}': "))

    elif opcion == 3:
        if not especialidades:
            print("No hay especialidades ingresadas.")
        else: 
            for i in range (len(especialidades)):
                    print(f"'{especialidades[i]}': {cupos[i]} cupos")

    elif opcion == 4:
        if not especialidades:
            print("No hay especialidades ingresadas.")
        else: 
            buscar = input("Ingrese la especialidad de la cual desea consultar la disponibilidad: ").lower()
            if buscar in especialidades: 
                indice = especialidades.index(buscar)
                print(f"'{buscar}' {cupos[indice]} cupos disponibles.")
            else: 
                print("Especialidad no encontrada.")

    elif opcion == 5:
        agotados = []
        if not especialidades:
            print("No hay especialidades ingresadas.")
        else:
            for i in range(len(especialidades)):
                if cupos[i] == 0:
                    agotados.append(especialidades[i])

            if agotados:
                print("\nEspecialidades sin cupos:")
                for especialidad in agotados:
                    print(f"-",especialidad)
            else: 
                print("Todas las especialidades tienen cupos disponibles.")

    elif opcion == 6:
        nueva_especialidad = input("Ingrese una nueva especialidad: ")
        if nueva_especialidad in especialidades:
            print("Ésta especialidad ya está agregada.")
        else:
            disponibilidad = int(input(f"Ingrese la cantidad de cupos para '{nueva_especialidad}': "))
            especialidades.append(nueva_especialidad)
            cupos.append(disponibilidad)
            print("Especialidad ingresada correctamente")

    elif opcion == 7:
        if not especialidades:
            print("No hay especialidades ingresadas.")
        else:
            actualizacion = input("Desea reservar (r) o cancelar (c) una cita? ").lower()
            especialidad_a_buscar = input("Ingrese el nombre de la especialidad: ").lower()

            if especialidad_a_buscar in especialidades:
                indice = especialidades.index(especialidad_a_buscar)
                if actualizacion == "r":
                    if cupos[indice] > 0:
                        cupos[indice] -= 1
                        print("Turno reservado correctamente. Lo esperamos!")
                    else: 
                        print("No hay turnos disponibles para esta especialidad.")
                elif actualizacion == "c":
                    cupos[indice] += 1
                    print("Turno cancelado correctamente")
                else:
                    print("Opción inválida")
            else:
                print("Especialidad no encontrada.")

    elif opcion == 8:
        if not especialidades:
            print("Agenda vacía.")
        else:
            print("\nAgenda completa del día:")
            #datetime.strptime convierte un string en un objeto datetime
            #("08.00", "%H:%M") indica el formato con hora en 24h y minutos
            hora_inicio = datetime.strptime("08:00", "%H:%M")
            for i in range(len(especialidades)):
                print(f"\nEspecialidad: {especialidades[i]}")
                print(f"Cupos disponibles: {cupos[i]}")
                print("Turnos del día:")
                hora = hora_inicio
                for j in range(cupos[i]):
                    #hora.strftime convierte el objeto datetime a un string legible
                    #hora + timedelta calcula 30 minutos después de la hora actual
                    print(f" - {hora.strftime('%H:%M')} a {(hora + timedelta(minutes=30)).strftime('%H:%M')}")
                    hora += timedelta(minutes=30)

    elif opcion == 9:
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida. Intente nuevamente")