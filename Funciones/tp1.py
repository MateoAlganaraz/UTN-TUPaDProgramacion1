import math

#1
def imprimir_hola_mundo():
    print("Hola Mundo!")

#2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#4a
def calcular_area_circulo(radio):
    return math.pi * radio**2

#4b
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#5
def segundos_a_horas(segundos):
    return segundos/3600

#6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

#7
def operaciones_basicas(a,b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b if b!=0 else None
    return(suma,resta,multiplicacion,division)

#8
def calcular_imc(peso, altura):
    if altura <= 0:
        return None 
    return peso/(altura**2)

#9
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

#10
def calcular_promedio(a,b,c):
    return(a+b+c)/3

#Validaciones para leer valores del usuario
def leer_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

def leer_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada no válida. Por favor ingresa un entero.")

#Programa principal para llamar a todas las funciones y pedir datos al usuario
def main():
    #1
    imprimir_hola_mundo()

    #2
    nombre = input("\nIntroduce tu nombre: ").strip()
    print(saludar_usuario(nombre))

    #3
    print("\n--- Información personal ---")
    nombre_p = input("Nombre: ").strip()
    apellido_p = input("Apellido: ").strip()
    edad_p = leer_int("Edad(años): ")
    residencia_p = input("Residencia (ciudad/pais): ").strip()
    informacion_personal(nombre_p, apellido_p, edad_p, residencia_p)

    #4
    print("\n--- Cálculo del círculo ---")
    radio = leer_float("Introduce el radío del círculo: ")
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área: {area:.4f}")
    print(f"Perímetro: {perimetro:.4f}")

    #5
    print("\n--- Segundos a horas ---")
    segundos = leer_float("Introduce la cantidad de segundos: ")
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos son {horas} horas.")

    #6
    print("n--- Tabla de multiplicar ---")
    numero_tabla = leer_int("Introduce el número para la tabla: ")
    tabla_multiplicar(numero_tabla)

    #7
    print("\n--- Operaciones básicas ---")
    a = leer_float("Introduce el primer número (a): ")
    b = leer_float("Introduce el segundo número (b): ")
    suma, resta, multiplicacion, division = operaciones_basicas(a,b)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    if division is None:
        print("División: No es posible dividir por cero.")
    else:
        print(f"División: {division}")

    #8
    print("\n--- Calcular IMC ---")
    peso = leer_float("Peso en kg: ")
    altura = leer_float("Altura en metros: ")
    imc = calcular_imc(peso, altura)
    if imc is None:
        print("Altura inválida para calcular IMC.")
    else:
        print(f"Tu IMC es: {imc:.2f}")

    #9
    print("\n--- Celsius a Fahrenheit ---")
    celsius = leer_float("Temperatura en Celsius: ")
    farenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C son {farenheit:.2f}°F")

    #10
    print("\n--- Calcular promedio ---")
    n1 = leer_float("Número 1: ")
    n2 = leer_float("Número 2: ")
    n3 = leer_float("Número 3: ")
    promedio = calcular_promedio(n1, n2, n3)
    print(f"El promedio es: {promedio}")

if __name__ == "__main__":
    main()