import csv
import os

def inicializar_archivo():
    if not os.path.exists('catalogo.csv'):
        with open('catalogo.csv', 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['TITULO', 'CANTIDAD'])
            escritor.writeheader()

def cargar_datos():
    lista = []
    if not os.path.exists('catalogo.csv'):
        return lista

    with open('catalogo.csv', 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                fila['CANTIDAD'] = int(fila['CANTIDAD'])
                if fila['CANTIDAD'] >= 0:
                    lista.append(fila)
            except ValueError:
                print(f'Datos inválidos en el archivo: {fila}')
    return lista

def actualizar_datos(lista):
    with open('catalogo.csv', 'w', newline= '', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['TITULO', 'CANTIDAD'])
        escritor.writeheader()
        escritor.writerows(lista)

def normalizar_titulos(titulo):
    return " ".join(titulo.strip().split()).lower()

def ingresar_titulos(lista):
    while True:
        cantidad = input("Cuántos libros desea ingresar? ")
        if not cantidad.isdigit():
            print("Debe ingresar un número entero positivo.")
            continue
        cantidad = int(cantidad)
        if cantidad <= 0:
            print("La cantidad debe ser mayor o igual a 0")
            continue
        break

    libros_agregados = 0
    for i in range(cantidad):
        print(f"\n--- Libro {i+1} de {cantidad} ---")
        while True:
            titulo = input("Título del libro: ").strip()
            if not titulo:
                print("El título no puede estar vacío.")
                continue

            titulo_normalizado = normalizar_titulos(titulo)
            duplicado = False
            for libro in lista:
                if normalizar_titulos(libro['TITULO']) == titulo_normalizado:
                    duplicado = True
                    break

            if duplicado:
                print("Ya existe un libro con ese título.")
                continue
            else:
                break

        while True:
            cantidad = input("Cantidad inicial: ")
            if not cantidad.isdigit():
                print("La cantidad debe ser un número entero no negativo.")
                continue
            cantidad_inicial = int(cantidad)
            if cantidad_inicial < 0:
                print("La cantidad debe ser mayor a 0.")
                continue
            break

        lista.append({'TITULO': titulo, 'CANTIDAD':cantidad_inicial})
        libros_agregados += 1

    if libros_agregados > 0:
        actualizar_datos(lista)
        print(f"Se agregaron {libros_agregados} libros correctamente.")
    return lista

def agregar_libro(lista):
    while True:
        titulo =input("Título del libro: ").strip()
        if not titulo:
            print("El título no puede estar vacío")
            continue
        titulo_normalizado = normalizar_titulos(titulo)
        duplicado = False
        for libro in lista:
            if normalizar_titulos(libro['TITULO']) == titulo_normalizado:
                duplicado = True
                break
        if duplicado:
            print("Ya existe un libro con ese título.")
            continue
        break

    while True:
        cantidad_ejemplares = input("Cantidad inicial de ejemplares: ")
        if not cantidad_ejemplares.isdigit():
            print("La cantidad debe ser un número entero no negativo.")
            continue
        cantidad = int(cantidad_ejemplares)
        if cantidad < 0:
            print("La cantidad debe ser mayor o igual a 0")
            continue
        break

    lista.append({'TITULO': titulo, 'CANTIDAD': cantidad})
    actualizar_datos(lista)
    print("Libro agregado correctamente.")
    return lista

def mostrar_inventario(lista):
    if not lista:
        print("No hay libros en el catálogo.")
    else:
        for libro in lista:
            print(f"- {libro['TITULO']} - {libro['CANTIDAD']} ejemplares.")

def editar_ejemplares(lista):
    titulo = input("Título del libro a editar: ").strip()
    if not titulo:
        print("Título inválido.")
        return lista
    
    titulo_normalizado = normalizar_titulos(titulo)
    for libro in lista:
        if normalizar_titulos(libro['TITULO']) == titulo_normalizado:
            while True:
                try:
                    nueva_cantidad = int(input("Nueva cantidad de ejemplares: "))
                    if nueva_cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                        continue
                    libro['CANTIDAD'] = nueva_cantidad
                    actualizar_datos(lista)
                    print("Cantidad actualizada correctamente.")
                    return lista
                except ValueError:
                    print("Debe ingresar un número entero.")
    print("Libro no encontrado.")
    return lista

def mostrar_sin_stock(lista):
    sin_stock = [libro for libro in lista if libro['CANTIDAD'] == 0]
    if not sin_stock:
        print("Todos los libros tienen ejemplares disponibles.")
    else:
        print("Libros agotados: ")
        for libro in sin_stock:
            print(f"- {libro['TITULO']}")

def prestar_devolver(lista):
    titulo = input("Título del libro: ").strip()
    if not titulo:
        print("Título inválido.")
        return lista
    
    titulo_normalizado = normalizar_titulos(titulo)
    for libro in lista:
        if normalizar_titulos(libro['TITULO']) == titulo_normalizado:
            print("1. Préstamo")
            print("2. Devolución")
            opcion = input("Seleccione una opción: ").strip()
            match opcion:
                case '1':
                    if libro['CANTIDAD'] <= 0:
                        print("No hay ejemplares disponibles para prestar.")
                    else:
                        libro['CANTIDAD'] -= 1
                        actualizar_datos(lista)
                        print(f"Préstamo realizado. Quedan {libro['CANTIDAD']} ejemplares.")
                    return lista
                case '2':
                    libro['CANTIDAD'] += 1
                    actualizar_datos()
                    print(f"Devolución registrada. Quedan {libro['CANTIDAD']} ejemplares.")
                    return lista
                case _:
                    print("Opción inválida.")
                    return lista
    print("Libro no encontrado.")
    return lista

def consultar_stock(lista):
    titulo = input("Título del libro a consultar: ").strip()
    if not titulo:
        print("Título inválido.")
        return
    
    titulo_normalizado = normalizar_titulos(titulo)
    for libro in lista:
        if normalizar_titulos(libro['TITULO']) == titulo_normalizado:
            print(f"Ejemplares disponibles: {libro['CANTIDAD']}")
            return 
    print("Libro no encontrado.")

def mostrar_menu():
    print("\n==== MENÚ BIBLIOTECA ESCOLAR ====")
    print("1. Ingresar títulos ")
    print("2. Editar cantidad")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar libro")
    print("7. Actualizar ejemplares")
    print("8. Salir")

def main():
    inicializar_archivo()
    catalogo = cargar_datos()
    while True:
        try:
            mostrar_menu()
            opcion = input("Seleccione una opción: ")

            match opcion:
                case '1':
                    catalogo = ingresar_titulos(catalogo)
                case '2':
                    catalogo = editar_ejemplares(catalogo)
                case '3':
                    mostrar_inventario(catalogo)
                case '4':
                    consultar_stock(catalogo)
                case '5':
                    mostrar_sin_stock(catalogo)
                case '6':
                    catalogo = agregar_libro(catalogo)
                case '7':
                    catalogo = prestar_devolver(catalogo)
                case '8':
                    print("Gracias por usar el sistema. Hata pronto!")
                    break
                case _:
                    print("Opción inválida. Por favor seleccione una opción del 1 al 8")
        except ValueError:
            print("Por favor ingrese un número.")

if __name__ == '__main__':
    main()