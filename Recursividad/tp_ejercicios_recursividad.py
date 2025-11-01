# Ejercicio 1
def factorial(n):
    """Calcula el factorial de n recursivamente."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def mostrar_factoriales(hasta):
    """Muestra el factorial de todos los números del 1 al 'hasta'"""
    print(f"\ Factoriales del 1 al {hasta}")
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")

#Ejercicio 2
def fibonacci(n):
    """Devuelve el valor de Fibonacci en la posición (0-indexed)."""
    if n <=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def mostrar_fibonacci(hasta):
    """Muestra la serie de Fibonacci hasta la posición 'hasta'."""
    print(f"\n Serie de Fibonacci hasta la posición {hasta}")
    for i in range(hasta+1):
        for i in range(hasta+1):
            print(f"F({i}) = {fibonacci(i)}")

#Ejercicio 3
def potencia(base, exponente):
    """Calcula la base exponente recursivamente"""
    if exponente == 0:
        return 1
    if exponente < 0:
        return 1/potencia(base, -exponente)
    return base * potencia(base, exponente - 1)

#Ejercicio 4
def decimal_a_binario(n):
    """Convierte un número decimal positivo a binario (como cadena)."""
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

#Ejercicio 5
def es_palindromo(palabra):
    """Verifica si una palabra es palíndromo (sin usar [::-1])."""
    #Caso base: cadena vacía o un solo caracter
    if len(palabra) <= 1:
        return True
    #Si los extremos coinciden, seguir con el interior
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    return False

#Ejercicio 6
def suma_digitos(n):
    """Suma los dígitos de un número entero positivo usando matemáticas."""
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

#Ejercicio 7
def contar_bloques(n):
    """Cuenta los bloques totales de una pirámide con n bloques en la base."""
    if n == 1:
        return 1
    return n + contar_bloques(n-1)

#Ejercicio 8
def contar_digito(numero, digito):
    """Cuenta cuántas veces aparece 'digito' en 'numero'"""
    if numero == 0:
        return 0
    ultimo = numero % 10
    resto = numero // 10
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)
    
#Menú interactivo para probar todas las funciones
def main():
    while True:
        print("\n" + "="*50)
        print("EJERCICIOS RECURSIVIDAD")
        print("="*50)
        print("1. Factorial")
        print("2. Serie de Fibonacci")
        print("3. Potencia")
        print("4. Decimal a Binario")
        print("5. Palíndromo")
        print("6. Suma de Dígitos")
        print("7. Bloques de Pirámide")
        print("8. Contar Dígito")
        print("9. Salir")
        print("="*50)
        opcion = input("Seleccione un ejercicio (1-9): ").strip()

        match opcion:
            case '1':
                n = int(input("Ingrese un número: "))
                mostrar_factoriales(n)
            case '2':
                n = int(input("Ingrese la posición máxima de Fibonacci: "))
                mostrar_fibonacci(n)
            case '3':
                base = float(input("Ingrese la base: "))
                exp = int(input("Ingrese el exponente: "))
                print(f"{base}^{exp} = {potencia(base,exp)}")
            case '4':
                n = int(input("Ingrese un número decimal positivo: "))
                if n < 0:
                    print("El número debe ser positivo.")
                else:
                    print(f"{n} en binario es: {decimal_a_binario(n)}")
            case '5':
                palabra = input("Ingrese una palabra (sin espacios ni tildes): ").strip().lower()
                if es_palindromo(palabra):
                    print(f"'{palabra}' es un palíndromo.")
                else:
                    print(f"'{palabra}' no es un palíndromo.")
            case '6':
                n = int(input("Ingrese un número entero positivo: "))
                if n < 0:
                    print(f"El número debe ser positivo.")
                else:
                    print(f"La suma de los dígitos de {n} es: {suma_digitos(n)}")
            case '7':
                n = int(input("Ingrese el número de bloques en la base: "))
                if n <= 0:
                    print("Debe ser un número positivo.")
                else:
                    print(f"Total de bloques en la pirámide: {contar_bloques(n)}")
            case '8':
                num = int(input("Ingrese un número entero positivo: "))
                dig = int(input("Ingrese un dígito (0-9): "))
                if num < 0 or dig > 9:
                    print("Valores inválidos.")
                else:
                    print(f"El dígito {dig} aparece {contar_digito(num,dig)} veces en {num}.")
            case '9':
                print("¡Gracias por practicar recursividad!")
                break
            case _:
                print("Opción inválida.")

if __name__ == "__main__":
    main()