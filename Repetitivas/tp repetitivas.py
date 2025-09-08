#EJERCICIO 1
for i in range(101):
    print(i)
    
#EJERCICIO 2
num = int(input("Ingresa un número entero: "))
cantidad_digitos = len(str(abs(num))) #Valor absoluto para ignorar el signo
print("El número tiene",cantidad_digitos,"dígitos.")

#EJERCICIO 3
num1 = int(input("Ingresa el primer: "))
num2 = int(input("Ingresa el segundo número: "))

#operador ternario
suma = sum(range(num1 + 1, num2)) if num1 < num2 else sum(range(num2 + 1, num1))
print(f"{num1} + {num2} = {suma}")

#EJERCICIO 4
total = 0
while True:
    n = int(input("Ingresa un número (0 para salir): "))
    if n == 0:
        break
    total += n
    
print("Total acumulado: ",total)

#EJERCICIO 5
import random

numero_secreto = random.randint(0,9)
intentos = 0

while True:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_secreto:
        break
    
print("¡CORRECTO! Número de intentos: ", intentos)

#EJERCICIO 6
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)
        
#EJERCICIO 7
num = int(input("Ingresa un número entero positivo: "))
suma = sum(range(num+1))
print(f"La suma de los números de 0 a {num} es: {suma}")

#EJERCICIO 8
pares = impares = positivos = negativos = 0

for i in range(100):
    num = int(input("Ingresa un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
        
print("\nPares", pares)
print("Impares", impares)
print("Positivos", positivos)
print("Negativos", negativos)

#EJERCICIO 9
total = 0 

for i in range(100):
    num = int(input("Ingresa un número: "))
    total += num
    
media = total/100
print("La media de los números ingresados es: ",media)

#EJERCICIO 10
num = input("Ingresa un número: ")
#[inicio:fin:paso] así funciona generalmente, lo que hacemos acá es declararlo vacío al inicio y al fin 
# y solo agregamos paso -1 para recorrerla de atrás para adelante a la cadena
invertido = num[::-1]
print("Número invertido: ",invertido)