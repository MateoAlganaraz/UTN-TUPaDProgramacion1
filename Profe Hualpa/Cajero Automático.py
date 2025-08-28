nombre = input("Nombre: ")
pin_verdadero = "141205"
saldo_disponible = 50000
contraseña = input("PIN: ")

if contraseña != pin_verdadero:
    print("PIN INCORRECTO. 2 intentos disponibles")
    contraseña = input("PIN: ")
    if contraseña != pin_verdadero:
      print("PIN INCORRECTO. 1 intento disponible")  
      contraseña = input("PIN: ")
      if contraseña != pin_verdadero:
        print("PIN INCORRECTO. 0 intentos disponibles. ADIOS!!")
        exit()

print(f"Bienvenido {nombre}")
print(f"Saldo disponible: ${saldo_disponible}")

eleccion = input("Escrbir: 'Retirar' o 'Cancelar' para salir: ").lower()

if eleccion == 'cancelar':
   print("Operacion cancelada.")
   exit()
else:
   monto_a_retirar = int(input("Monto a retirar: "))
   if monto_a_retirar > saldo_disponible:
      print("No puedes superar el saldo disponible")
      exit()
   elif monto_a_retirar % 1000 != 0:
      print("El monto debe ser múltiplo de 1000")
      exit()
   elif monto_a_retirar > 20000:
      monto_a_retirar = monto_a_retirar+monto_a_retirar*0.2
      print("Al retirar más de $20000 se le cobra una comisión del 2%")
      if monto_a_retirar > saldo_disponible:
         print("No puedes superar el saldo disponible") 

saldo_disponible=saldo_disponible-monto_a_retirar

print(f"\nNombre: {nombre}")
print(f"Dinero retirado: {monto_a_retirar}")
print(f"Saldo disponible actualizado: {saldo_disponible}")
