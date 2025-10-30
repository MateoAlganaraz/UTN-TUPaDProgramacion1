import csv
import os

# --- Constantes ---
NOMBRE_ARCHIVO = 'Casos Parciales/inventario.csv'
CAMPOS = ['nombre', 'stock', 'precio']

# --- Funciones de Utilidad y Archivo ---

def inicializar_inventario():
    """
    Intenta leer el inventario del archivo CSV. Si no existe, devuelve una lista vacía.
    """
    inventario = []
    try:
        # Verifica si el archivo existe antes de intentar leer
        if not os.path.exists(NOMBRE_ARCHIVO):
            print(f"Archivo '{NOMBRE_ARCHIVO}' no encontrado. Se creará uno nuevo al guardar.")
            return inventario

        with open(NOMBRE_ARCHIVO, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    # Convertir stock y precio a sus tipos correctos
                    fila['stock'] = int(fila['stock'])
                    fila['precio'] = float(fila['precio'])
                    inventario.append(fila)
                except ValueError as e:
                    print(f"Error al convertir datos en el archivo CSV para la fila: {fila}. Error: {e}")
                    # Se podría optar por omitir la fila o corregirla, aquí la omitimos.
            print(f"Inventario cargado: {len(inventario)} herramientas.")
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
    return inventario

def guardar_inventario(inventario):
    """
    Escribe el inventario completo (lista de diccionarios) en el archivo CSV.
    """
    try:
        with open(NOMBRE_ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()  # Escribe la primera fila (encabezados)
            escritor.writerows(inventario)
        print(f"Inventario guardado exitosamente en '{NOMBRE_ARCHIVO}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo CSV: {e}")

def buscar_herramienta_por_nombre(inventario, nombre):
    """
    Busca una herramienta por nombre.
    Retorna la herramienta y su índice, o (None, -1) si no se encuentra.
    """
    for i, herramienta in enumerate(inventario):
        if herramienta['nombre'].strip().lower() == nombre.strip().lower():
            return herramienta, i
    return None, -1

# --- Funciones del Menú ---

def cargar_herramientas(inventario):
    """Opción 1: Carga y registra una nueva herramienta."""
    print("\n--- Cargar Herramienta ---")
    while True:
        nombre = input("Ingrese nombre: ").strip()
        if nombre:
            # Validar que el nombre no exista
            if buscar_herramienta_por_nombre(inventario, nombre)[0] is not None:
                print("Error: Esta herramienta ya existe en el inventario.")
                return
            break
        print("El nombre no puede estar vacío.")

    while True:
        try:
            stock = int(input("Ingrese stock (entero >= 0): "))
            if stock < 0:
                print("El stock debe ser un entero positivo o cero.")
                continue
            break
        except ValueError:
            print("Entrada inválida. El stock debe ser un número entero.")

    while True:
        try:
            precio = float(input("Ingrese precio (float > 0): "))
            if precio <= 0:
                print("El precio debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. El precio debe ser un número.")

    nueva_herramienta = {
        'nombre': nombre,
        'stock': stock,
        'precio': precio
    }
    inventario.append(nueva_herramienta)
    guardar_inventario(inventario) # Guardar en CSV inmediatamente
    print(f"Herramienta '{nombre}' registrada correctamente.")

def mostrar_herramientas_registradas(inventario):
    """Opción 2: Muestra todas las herramientas del inventario."""
    print("\n--- Herramientas Registradas ---")
    if not inventario:
        print("El inventario está vacío.")
        return

    print(f"{'NOMBRE':<20} | {'STOCK':>6} | {'PRECIO':>10}")
    print("-" * 40)
    for h in inventario:
        print(f"{h['nombre']:<20} | {h['stock']:>6} | ${h['precio']:>9.2f}")

def modificar_herramienta(inventario):
    """Opción 3: Permite cambiar el stock o el precio de una herramienta."""
    print("\n--- Modificar Herramienta ---")
    nombre_modificar = input("Ingrese el nombre de la herramienta a modificar: ").strip()
    herramienta, indice = buscar_herramienta_por_nombre(inventario, nombre_modificar)

    if herramienta is None:
        print(f"Error: Herramienta '{nombre_modificar}' no encontrada.")
        return

    print(f"Herramienta actual: Stock: {herramienta['stock']} | Precio: ${herramienta['precio']:.2f}")

    # Modificar Stock
    while True:
        nuevo_stock_str = input("Nuevo stock (dejar vacío para no cambiar): ").strip()
        if not nuevo_stock_str:
            break
        try:
            nuevo_stock = int(nuevo_stock_str)
            if nuevo_stock < 0:
                print("El stock debe ser un entero positivo o cero.")
                continue
            inventario[indice]['stock'] = nuevo_stock
            print(f"Stock actualizado a {nuevo_stock}.")
            break
        except ValueError:
            print("Entrada inválida. El stock debe ser un número entero.")

    # Modificar Precio
    while True:
        nuevo_precio_str = input("Nuevo precio (dejar vacío para no cambiar): ").strip()
        if not nuevo_precio_str:
            break
        try:
            nuevo_precio = float(nuevo_precio_str)
            if nuevo_precio <= 0:
                print("El precio debe ser un número positivo.")
                continue
            inventario[indice]['precio'] = nuevo_precio
            print(f"Precio actualizado a ${nuevo_precio:.2f}.")
            break
        except ValueError:
            print("Entrada inválida. El precio debe ser un número.")

    guardar_inventario(inventario)
    print("Datos de la herramienta actualizados.")

def eliminar_herramienta(inventario):
    """Opción 4: Elimina una herramienta del inventario por nombre."""
    print("\n--- Eliminar Herramienta ---")
    nombre_eliminar = input("Ingrese el nombre de la herramienta a eliminar: ").strip()
    herramienta, indice = buscar_herramienta_por_nombre(inventario, nombre_eliminar)

    if herramienta is None:
        print(f"Error: Herramienta '{nombre_eliminar}' no encontrada.")
        return

    # Confirmación
    confirmacion = input(f"¿Está seguro que desea eliminar '{herramienta['nombre']}'? (s/n): ").lower()
    if confirmacion == 's':
        inventario.pop(indice)
        guardar_inventario(inventario)
        print(f"Herramienta '{herramienta['nombre']}' eliminada correctamente.")
    else:
        print("Eliminación cancelada.")

def consultar_disponibilidad(inventario):
    """Opción 5: Muestra cuántas unidades hay disponibles de una herramienta."""
    print("\n--- Consultar Disponibilidad ---")
    nombre_consulta = input("Ingrese el nombre de la herramienta a consultar: ").strip()
    herramienta, _ = buscar_herramienta_por_nombre(inventario, nombre_consulta)

    if herramienta is None:
        print(f"Error: Herramienta '{nombre_consulta}' no encontrada.")
        return

    print(f"Disponibilidad de '{herramienta['nombre']}': **{herramienta['stock']}** unidades.")

def listar_sin_stock(inventario):
    """Opción 6: Muestra todas las herramientas cuyo stock sea igual a 0."""
    print("\n--- Listar Productos Sin Stock (Stock = 0) ---")
    sin_stock = [h for h in inventario if h['stock'] == 0]

    if not sin_stock:
        print("¡Todo en stock! No hay herramientas agotadas.")
        return

    print(f"{'NOMBRE':<20} | {'PRECIO':>10}")
    print("-" * 32)
    for h in sin_stock:
        print(f"{h['nombre']:<20} | ${h['precio']:>9.2f}")

# --- Desafío Extra ---
def buscar_por_precio_mayor_a(inventario):
    """Opción 8: Busca herramientas con precio mayor a un valor ingresado."""
    print("\n--- Buscar Por Precio Mayor A ---")
    while True:
        try:
            precio_limite = float(input("Ingrese el precio mínimo para la búsqueda: "))
            if precio_limite <= 0:
                print("El precio debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Debe ser un número.")

    herramientas_encontradas = [h for h in inventario if h['precio'] > precio_limite]

    if not herramientas_encontradas:
        print(f"No se encontraron herramientas con precio mayor a ${precio_limite:.2f}.")
        return

    print(f"\n--- Herramientas con Precio > ${precio_limite:.2f} ---")
    print(f"{'NOMBRE':<20} | {'STOCK':>6} | {'PRECIO':>10}")
    print("-" * 40)
    for h in herramientas_encontradas:
        print(f"{h['nombre']:<20} | {h['stock']:>6} | ${h['precio']:>9.2f}")


# --- Funciones de menú y main ---

def mostrar_menu():
    """
    Muestra el menú interactivo y solicita una opción al usuario
    Retorna la opción ingresada como string
    """
    print("\n===== MENÚ FERRETERÍA =====")
    print("1. Cargar herramientas")
    print("2. Mostrar herramientas registradas")
    print("3. Modificar herramienta")
    print("4. Eliminar herramienta")
    print("5. Consultar disponibilidad")
    print("6. Listar productos sin stock")
    print("7. Buscar por precio (Desafío Extra)")
    print("8. Salir")
    return input("Seleccione una opción: ").strip()

def main():
    """
    Función principal que incializa el inventario y gestiona las opciones del menú.
    """
    inventario = inicializar_inventario()

    while True:
        opcion = mostrar_menu()

        match opcion:
            case '1':
                cargar_herramientas(inventario)
            case '2':
                mostrar_herramientas_registradas(inventario)
            case '3':
                modificar_herramienta(inventario)
            case '4':
                eliminar_herramienta(inventario)
            case '5':
                consultar_disponibilidad(inventario)
            case '6':
                listar_sin_stock(inventario)
            case '7':
                buscar_por_precio_mayor_a(inventario)
            case '8':
                print("\n Programa finalizado. ¡Hasta pronto!")
                break
            case _:
                print("Opción inválida. Ingrese un número del 1 al 8.")

if __name__ == "__main__":
    main()