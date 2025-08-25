clases = {
   "lunes": "nivel inicial",
    "martes": "nivel intermedio",
    "miercoles": "nivel avanzado",
    "jueves": "práctica hablada",
    "viernes": "inglés para viajeros",
}

dias_validos = list(clases.keys())

fecha_actual = input("Ingrese la fecha en formato 'día, DD/MM: ")

dia_semana, fecha = fecha_actual.split(", ")
dia_semana = dia_semana.lower()

if dia_semana not in dias_validos:
    print("ERROR: El día de la semana no es válido")
    exit()

dia,mes = fecha.split("/")
dia = int(dia)
mes = int(mes)

if not (1 <= dia <= 31 and 1 <= mes <= 12):
    print("ERROR: La fecha no es válida")
    exit()

nivel = clases[dia_semana]
print(f"Hoy es {dia_semana.capitalize()}({nivel}).")

if nivel in ["nivel inicial", "nivel intermedio", "nivel avanzado"]:

    hubo_examen = input("¿Se tomaron exámenes hoy? (si/no): ").lower()
    if hubo_examen == "si":
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
        total_alumnos = aprobados + desaprobados
        if total_alumnos > 0:
            porcentaje_aprobados = (aprobados/total_alumnos)*100
            print(f"El porcentaje total de aprobados es: {porcentaje_aprobados:.2f}%")
        else:
            print("No hubo alumnos cargados")
    else:
        print("Suerte en tu próximo exámen! ")

elif nivel == "práctica hablada":
    asistencia = float(input("Ingrese el porcentaje de asistencia: "))
    if asistencia >= 50: 
        print("Asistió la mayoría")
    else:
        print("No asistió la mayoría")

elif nivel == "inglés para viajeros":
    if dia == 1 and (mes == 1 or mes == 7):
        print("Buen comienzo de ciclo!! ")
        alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel = float(input("Ingrese el arancel por alumno en $: "))
        ingreso_total = alumnos * arancel
        print(f"Ingreso total del ciclo: ${ingreso_total:.2f}")