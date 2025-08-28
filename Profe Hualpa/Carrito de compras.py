medio_de_pago = {
    1 : "Efectivo",
    2 : "Débito",
    3 : "Crédito",
    4 : "Mercado pago"
}

nombre = input("Nombre: ")
cantidad_productos = input("Cuántos productos quiere comprar? ")

if not cantidad_productos.isdigit():
    print("Debe ingresar un número entero") 
    exit()

cantidad_productos = int(cantidad_productos)  
  
if cantidad_productos <= 0:
    print("La cantidad de productos debe ser mayor que 0")
    exit()

monto = float(input("Monto total de la compra: ")) 

if monto <= 0:
    print("El monto debe ser mayor a 0")
    exit()
    
pago = int(input("Medio de pago (1= Efectivo, 2= Débito, 3= Crédito, 4= Mercado pago): "))
total_a_pagar = monto

if pago == 1:
    print("\nDescuento del 15% por pagar en efectivo")
    total_a_pagar -= monto*0.15
elif pago == 2:
    print("\nDescuento del 10% por pagar en efectivo")
    total_a_pagar -= monto*0.10
elif pago == 3:
    print("\nRecargo del 5% por pagar con crédito")
    total_a_pagar += monto*0.05
elif pago == 4:
    if monto > 10000:
        print("\nDescuento del 20% por pagar con mercado pago en una compra de más de $10000")
        total_a_pagar -= monto*0.2
else:
    print("Medio de pago inválido")
    exit()
        
if cantidad_productos > 10:
    print("Descuento del 5% por llevar más de 10 productos")
    total_a_pagar -= total_a_pagar*0.05

print("\nRESUMEN DE COMPRA")
print(f"Cliente: {nombre}")
print(f"Productos: ")
print(f"Medio de pago: {medio_de_pago.get(pago, 'Desconocido')}")
print(f"Monto original: ${monto:,.2f}")
print(f"Importe final a pagar: ${total_a_pagar:,.2f}")