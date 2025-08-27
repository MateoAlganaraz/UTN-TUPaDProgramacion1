prioridad = {
    1 : "Emergencia", 
    2 : "Urgente",
    3 : "Control"
}

nombre_completo = input("Nombre y apellido: ")
documento = input("DNI (sin puntos ni espacios): ")

if len(documento) not in (7,8):
    print("El documento debe tener mínimo 7 dígitos")
    exit()
elif not documento.isdigit():
    print("El DNI solo debe contener números")
    exit()

edad = int(input("Edad: "))
obra_social = input("Obra social? (si/no): ").lower()

if obra_social not in ("si","no"):
    print("Por favor solo ingrese por si o por no")
    exit()

prioridad = int(input("1 = emergencia, 2 = urgente, 3 = control: "))

if prioridad == 1:
    turno = "Asignado inmediatamente a guardia"
elif prioridad == 2:
    if obra_social == "si":
        turno = "Turno en menos de 24hs"
    else:
        turno = "Turno en 48hs"
elif prioridad == 3:
    if edad > 65:
        turno = "Turno preferencial en 72hs"
    else:
        turno = "Turno normal en 7 días"
else:
    turno = "Prioridad inválida"

print("")
print(f"Nombre: {nombre_completo}")
print(f"DNI: {documento}")
print(f"Edad: {edad}")
print(f"Prioridad: {prioridad}")
print(f"Turno asignado: {turno}")