estudiante = {
    "nombre": input("Nombre y apellido: "),
    "edad": int(input("Edad: ")),
    "promedio": float(input("Promedio (0-10): ")),
    "ingresos": int(input("Ingresos familiares mensuales: "))
}

if estudiante["edad"] < 1:
    print("Edad inválida. Debe ser mayor a 0")
elif estudiante["promedio"] < 0 or estudiante["promedio"] > 10:
    print("Promedio inválido. Debe estar entre 0 y 10")
elif estudiante["ingresos"] < 0:
    print("Ingresos inválidos. No se puede ser negativo")
else:
    if estudiante["promedio"] < 6:
        estudiante["resultado"] = "Rechazado"
    elif estudiante["ingresos"] < 300000:
        estudiante["resultado"] = "Beca completa"
    elif estudiante["ingresos"] <= 600000:
        estudiante["resultado"] = "Media beca"
    else:
        estudiante["resultado"] = "Rechazado"

print(f"{estudiante['nombre']}, {estudiante['edad']} años")
print(f"Promedio: {estudiante['promedio']}")
print(f"Ingresos: {estudiante['ingresos']}")
print(f"Resultado: {estudiante['resultado']}")