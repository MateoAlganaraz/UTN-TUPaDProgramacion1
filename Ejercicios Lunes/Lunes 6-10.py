def crear_mochila():
    """Solicitamos al usuario el tamaño de la mochila y validamos la entrada."""

    while True:
        try:
            tamanio = int(input("Ingresa cuántos espacios tendrá la mochila: "))
            if tamanio <= 0:
                print("Error: El número debe ser positivo. Inténtalo de nuevo.")
                continue
            return ["--- vacío ---"] * tamanio
        except ValueError:
            print("Error: Debes ingresar un número entero válido. Inténtalo de nuevo.")

def guardar_objeto(mochila):
    """Permitimos al usuario guardar un objeto en una posición específica."""

    try:
        posicion = int(input(f"Ingresa la posición (0-{len(mochila)-1}): "))
        objeto = input("Ingresa el objeto mágico: ").strip()
        
        if not objeto:
            print("Error: No puedes guardar un objeto vacío.")
            return
        
        mochila[posicion] = objeto
        print(f"{objeto} guardado en el espacio {posicion}")
        
    except IndexError:
        print(f"Error: La posición debe estar entre 0 y {len(mochila)-1}.")
    except ValueError:
        print("Error: Debes ingresar un número entero para la posición.")

def ver_mochila(mochila):
    """Mostramos el contenido actual de la mochila."""

    print("\nContenido de la mochila:")
    #enumerate(mochila) agrega un contador(índice) a cada elemento de un iterable para obtener pares de (índice,valor)
    #i toma los valores de los índices
    #item toma los valores de los objetos
    for i, item in enumerate(mochila):
        print(f"Espacio {i}: {item}")

def eliminar_objeto(mochila):
    """Permitimos al usuario eliminar un objeto de una posición específica."""

    try:
        posicion = int(input(f"Ingresa la posición (0-{len(mochila)-1}) para eliminar: "))
        
        if mochila[posicion] == "--- vacío ---":
            print(f"El espacio {posicion} ya está vacío.")
        else:
            mochila[posicion] = "--- vacío ---"
            print(f"Objeto eliminado del espacio {posicion}.")
            
    except IndexError:
        print(f"Error: La posición debe estar entre 0 y {len(mochila)-1}.")
    except ValueError:
        print("Error: Debes ingresar un número entero para la posición.")

def main():
    print("¡Bienvenido al organizador de mochila mágica!\n")
    
    # Parte 1: Crear la mochila
    mochila = crear_mochila()
    
    # Parte 2: Menú principal
    while True:
        print("\n--- Menú de la Mochila ---")
        print("1. Guardar objeto")
        print("2. Ver mochila")
        print("3. Eliminar objeto")  # Desafío extra
        print("4. Salir")
        
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Error: Debes ingresar un número del menú.")
            continue
        
        if opcion == 1:
            guardar_objeto(mochila)
        elif opcion == 2:
            ver_mochila(mochila)
        elif opcion == 3:
            eliminar_objeto(mochila)
        elif opcion == 4:
            print("¡Gracias por usar la mochila mágica! ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()