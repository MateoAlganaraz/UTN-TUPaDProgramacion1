def leer_productos(archivo="productos.txt"):
    """Lee el archivo y devuelve una lista de diccionarios."""
    productos = []
    try:
        with open(archivo, mode='r', encoding='utf-8') as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) == 3:
                    try:
                        nombre = partes[0]
                        precio = float(partes[1])
                        cantidad = int(partes[2])
                        productos.append({
                            "nombre": nombre,
                            "precio": precio,
                            "cantidad": cantidad
                        })
                    except ValueError:
                        print(f"Advertencia: Línea con formato inválido ignorada: {linea.strip()}")
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe. Se creará al agregar el primer producto.")
    return productos

def guardar_productos(productos, archivo="productos.txt"):
    """Sobrescribe el archivo con todos los productos actuales."""
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            for p in productos:
                f.write(f"{p['nombre']}, {p['precio']}, {p['cantidad']}\n")
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar: {e}")

def mostrar_productos(productos):
    """Muestra los productos en formato legible."""
    if not productos:
        print("No hay productos registrados.")
        return
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

def agregar_producto(productos):
    """Solicita los datos al usuario y agrega un nuevo producto a la lista."""
    print("\n--- Agregar nuevo producto ---")
    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    
    #Verificar duplicados (opcional pero útil)
    for p in productos:
        if p["nombre"].lower() == nombre.lower():
            print("Ya existe un producto con ese nombre.")
            return
        
    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        if precio < 0 or cantidad < 0:
            print("Precio y cantidad deben ser valores no negativos.")
            return
    except ValueError:
        print("Precio o cantidad inválidos.")
        return
    
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print("Producto agregado.")

def buscar_producto(productos):
    """Busca un producto por nombre e imprime sus datos."""
    if not productos:
        print("No hay productos para buscar.")
        return
    
    nombre_buscar = input("\nIngrese el nombre del producto a buscar: ").strip()
    if not nombre_buscar:
        print("Nombre inválido.")
        return
    
    for p in productos:
        if p["nombre"].lower() == nombre_buscar.lower():
            print(f"\n Producto encontrado:")
            print(f"Nombre: {p["nombre"]}")
            print(f"Precio: ${p["precio"]}")
            print(f"Cantidad: {p["cantidad"]}")
            return
        
    print(f"No se encontró ningún producto con el nombre '{nombre_buscar}'.")

def main():
    #1. Leer productos desde el archivo
    productos = leer_productos()

    #2. Mostrar productos
    print("=== PRODUCTOS ACTUALES ===")
    mostrar_productos(productos)

    #3. Agregar un nuevo producto
    agregar_producto(productos)

    #4. Ya están cargados en lista de diccionarios (hecho en leer_productos)

    #5.Buscar producto por nombre
    buscar_producto(productos)

    #6. Guardar todos los productos actualizados
    guardar_productos(productos)

    print("\n Programa finalizado. ¡Gracias!")

if __name__ == "__main__":
    main()