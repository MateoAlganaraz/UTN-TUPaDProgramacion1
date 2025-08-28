historial_dict = {
    1 : "Bueno",
    2: "Regular",
    3: "Malo"
}

nombre_completo = input("Nombre y apellido: ")
cuit = input("CUIT 'Formato xx-xxxxxxxx-x': ")

if len(cuit) not in (13,):
    print("El CUIT debe llevar 11 dígitos y dos guiones")
    exit()
elif cuit[2] != "-" or cuit[11] != "-":
    print("El CUIT debe llevar guiones")
    exit()
elif not (cuit[0:2].isdigit() and cuit[3:11].isdigit() and cuit[12].isdigit()):
    print("El CUIT solo debe llevar números")
    exit()

ingresos_mensuales = int(input("Ingresos mensuales: "))
antiguedad_laboral = int(input("Años en la empresa: "))
historial_num = int(input("Historial crediticio: 1 = bueno/ 2 = regular / 3 = malo: "))

historial_texto = historial_dict.get(historial_num, "Este valor no existe")

if historial_num == 3:
    monto_aprobado = "Rechazado"
elif ingresos_mensuales < 200000:
    monto_aprobado = "Rechazado"
elif ingresos_mensuales >= 200000 and antiguedad_laboral < 2:
    monto_aprobado = "$500.000"
elif ingresos_mensuales >= 200000 and antiguedad_laboral >= 2:
    if historial_num == 2:
        monto_aprobado = "$1.000.000"
    elif historial_num == 1:
        monto_aprobado = "$3.000.000"

print(f"\nCliente: {nombre_completo}")
print(f"CUIT: {cuit}")
print(F"Ingresos: {ingresos_mensuales}")
print(f"Antigüedad: {antiguedad_laboral}")
print(f"Historial {historial_texto}")
print(f"Monto aprobado: {monto_aprobado}")