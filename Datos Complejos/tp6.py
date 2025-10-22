#Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

"""Añadimos nuevas frutas"""
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario actualizado: ", precios_frutas)

#Actividad 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Precios actualizados:",precios_frutas)

#Actividad 3
"""Extraemos solo las claves (nombres de frutas)"""
frutas = list(precios_frutas.keys())

print("Lista de frutas: ", frutas)

#Actividad 4
contactos = {}

"""Cargar 5 contactos"""
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ").strip()
    numero = input(f"Ingrese el número de {nombre}: ").strip()
    contactos[nombre] = numero

"""Consultar un número"""
consulta = input("Ingrese el nombre del contacto a buscar: ").strip()
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print("Contacto no encontrado.")

#Actividad 5
frase = input("Ingrese una frase: ").strip()

"""Dividir en palabras y convertir a minúsculas"""
palabras = frase.lower().split()

"""Palabras únicas (set)"""
palabras_unicas = set(palabras)

"""Conteo de frecuencia"""
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0)+1

print("\nPalabras únicas: ", palabras_unicas)
print("Recuento: ",recuento)

#Actividad 6
alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ").strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

"""Mostrar promedio de cada alumno"""
print(f"\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas)/len(notas)
    print(f"{nombre}: {promedio:.2f}")

#Actividad 7
"""Supongamos estos sets"""
aprobados_par1 = {"Ana", "Juan", "Luis", "Marta"}
aprobados_par2 = {"Juan", "Marta", "Pedro", "Sofía"}

"""Ambos parciales"""
ambos = aprobados_par1 & aprobados_par2 #Intersección
print("Aprobaron ambos parciales:",ambos)

"""Solo uno de los dos"""
solo_uno = aprobados_par1 ^ aprobados_par2 #Diferencia simétrica
print("Aprobaron solo uno de los dos: ", solo_uno)

"""Total sin repetir"""
total = aprobados_par1 | aprobados_par2 #Unión
print("Total de estudiantes que aprobaron al menos uno: ",total)

#Actividad 8
stock = {}

while True:
    print("\n--- Menú Stock ---")
    print("1. Consultar stock")
    print("2. Agregar unidades")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    opcion = input("Seleccione opción: ")

    match opcion:
        case "1":
            producto = input("Nombre del producto: ")
            if producto in stock:
                print(f"Stock de {producto}: {stock[producto]}")
            else:
                print("Producto no encontrado.")

        case "2":
            producto = input("Nombre del producto: ")
            if producto in stock:
                try:
                    cantidad = int(input("Unidades a agregar: "))
                    if cantidad >= 0:
                        stock[producto] += cantidad
                        print(f"Stock actualizado: {stock[producto]}")
                    else:
                        print("La cantidad debe ser no negativa.")
                except ValueError:
                    print("Por favor, ingrese un número entero válido.")
            else:
                print("Producto no existe.")

        case "3":
            producto = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad inicial: "))
                if cantidad >= 0:
                    stock[producto] = cantidad
                    print(f"Producto '{producto}' agregado con stock {cantidad}.")
                else:
                    print("La cantidad debe ser no negativa.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

        case "4":
            print("Saliendo del sistema de stock.")
            break

        case _:
            print("Opción inválida. Por favor, seleccione 1, 2, 3 o 4.")

#Actividad 9
agenda = {}

while True:
    print("\n--- Agenda ---")
    print("1. Agregar evento")
    print("2. Consultar evento")
    print("3. Salir")
    opcion = input("Opción: ").strip()

    match opcion:
        case "1":
            dia = input("Día (ej: lunes): ").strip()
            hora = input("Hora (ej: 10:00): ").strip()
            evento = input("Evento: ").strip()
            agenda[(dia, hora)] = evento
            print("Evento agregado.")

        case "2":
            dia = input("Día a consultar: ").strip()
            hora = input("Hora a consultar: ").strip()
            clave = (dia, hora)
            if clave in agenda:
                print(f"Actividad: {agenda[clave]}")
            else:
                print("No hay actividad programada.")

        case "3":
            print("¡Hasta luego!")
            break

        case _:
            print("Opción inválida. Por favor, elija 1, 2 o 3.")

#Actividad 10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}

"""Creamos el diccionario invertido"""
invertido = {capital:pais for pais, capital in original.items()}

print("Original:", original)
print("Invertido:",invertido)