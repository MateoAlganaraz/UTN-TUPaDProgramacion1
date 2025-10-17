import csv
import os

# Nombre del archivo CSV
ARCHIVO = "productos.csv"
ENCABEZADOS = ["nombre", "precio"]


def crear_archivo_si_no_existe():
    """Crea el archivo CSV con encabezados si no existe."""
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADOS)
            escritor.writeheader()


def cargar_productos():
    """Carga todos los productos desde el archivo CSV."""
    productos = []
    try:
        with open(ARCHIVO, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    # Convertir precio a float para operaciones numéricas
                    fila['precio'] = float(fila['precio'])
                    productos.append(fila)
                except (ValueError, KeyError):
                    print(f"  Advertencia: dato inválido ignorado: {fila}")
    except FileNotFoundError:
        # No debería ocurrir gracias a crear_archivo_si_no_existe(), pero por seguridad
        pass
    return productos


def guardar_productos(productos):
    """Guarda la lista completa de productos en el archivo CSV (sobrescribe)."""
    try:
        with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADOS)
            escritor.writeheader()
            escritor.writerows(productos)
    except Exception as e:
        print(f"Error al guardar los productos: {e}")


def mostrar_productos():
    """Muestra todos los productos y el total de precios."""
    productos = cargar_productos()
    if not productos:
        print("No hay productos registrados.")
        return

    print("Productos registrados:")
    total = 0.0
    for p in productos:
        print(f"- {p['nombre']} → ${p['precio']:.2f}")
        total += p['precio']
    print(f"Total de precios: ${total:.2f}")


def agregar_producto():
    """Agrega un nuevo producto al archivo."""
    nombre = input("Ingrese el nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    while True:
        try:
            precio_str = input("Ingrese el precio: ").strip()
            precio = float(precio_str)
            if precio <= 0:
                print("El precio debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Cargar productos actuales, agregar el nuevo y guardar
    productos = cargar_productos()
    productos.append({"nombre": nombre, "precio": precio})
    guardar_productos(productos)
    print("Producto agregado correctamente.")


def eliminar_producto():
    """Elimina un producto por nombre. Solicita nombre hasta que sea válido o existente."""
    productos = cargar_productos()
    if not productos:
        print("No hay productos registrados. Agregue al menos uno antes de eliminar.")
        return

    while True:
        nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue

        # Buscar si existe (insensible a mayúsculas)
        for p in productos:
            if p['nombre'].lower() == nombre.lower():
                # Filtrar y guardar sin ese producto
                productos_actualizados = [p for p in productos if p['nombre'].lower() != nombre.lower()]
                guardar_productos(productos_actualizados)
                print("Producto eliminado correctamente.")
                return  # Salir de la función

        # Si llega aquí, no se encontró
        print("Producto no encontrado. Intente con un nombre existente.")


def actualizar_precio():
    """Actualiza el precio de un producto existente. Solicita nombre hasta que sea válido."""
    productos = cargar_productos()
    if not productos:
        print("No hay productos registrados. Agregue al menos uno antes de actualizar.")
        return

    while True:
        nombre = input("Ingrese el nombre del producto a actualizar: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue

        # Buscar el producto
        for p in productos:
            if p['nombre'].lower() == nombre.lower():
                # Producto encontrado → pedir nuevo precio (con validación)
                while True:
                    try:
                        nuevo_precio_str = input(f"Ingrese el nuevo precio para '{p['nombre']}': ").strip()
                        nuevo_precio = float(nuevo_precio_str)
                        if nuevo_precio <= 0:
                            print("El precio debe ser un número positivo.")
                            continue
                        p['precio'] = nuevo_precio
                        guardar_productos(productos)
                        print("Precio actualizado correctamente.")
                        return
                    except ValueError:
                        print("Por favor, ingrese un número válido.")

        # Si no se encontró
        print("Producto no encontrado. Intente con un nombre existente.")


def mostrar_menu():
    """Muestra el menú principal."""
    print("\n====== MENÚ DE PRODUCTOS ======")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Actualizar precio")  # Desafío extra
    print("5. Salir")
    print("===============================")


def main():
    """Función principal que gestiona el menú y las operaciones."""
    crear_archivo_si_no_existe()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                mostrar_productos()
            case "2":
                agregar_producto()
            case "3":
                eliminar_producto()
            case "4":
                actualizar_precio()  # Desafío extra
            case "5":
                print("¡Gracias por usar el sistema!")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()