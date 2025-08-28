nombre_completo = input("Nombre y apellido: ")
edad = int(input("Edad: "))
ingresos = float(input("Ingresos anuales: "))

if ingresos < 500000:
    a_pagar = 0
elif ingresos >= 500000 and ingresos < 2000000:
    a_pagar = ingresos*0.10
elif ingresos >= 2000000 and ingresos < 5000000:
    a_pagar = ingresos*0.20
elif ingresos >= 5000000:
    a_pagar = ingresos*0.35

if edad > 65:
    a_pagar = a_pagar/2
    print("Descuento del 50% por ser mayor de 65 años")

print("")
print(f"Nombre: {nombre_completo}")
print(f"Edad: {edad}")
print(f"Ingresos anuales: {ingresos:,.2f}")
print(f"Impuesto final: {a_pagar:,.2f}")