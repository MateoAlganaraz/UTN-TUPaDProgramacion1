monto_total = float(input("Ingrese el monto total de la cuenta: "))
propina10 = monto_total*0.10
propina15 = monto_total*0.15
print(f"Propina sugerida(10%): {propina10}")
print("Total a pagar: ",monto_total+propina10)
print(f"Propina sugerida(15%): {propina15}")
print("Total a pagar: ",monto_total+propina15)
