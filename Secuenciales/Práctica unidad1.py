#Ejercicio 1
print("Hola mundo!")

#Ejercicio 2
nombre = input("Ingrese su nombre por favor: ")
print(f"Su nombre es {nombre}")

#Ejercicio 3
nombre, apellido, edad, lugar_de_residencia = input("Ingrese su nombre por favor: "), input("Ingrese su apellido: "), input("Ingrese su edad: "), input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre}{apellido} tengo {edad} y resido en {lugar_de_residencia}")

#Ejercicio 4
radio = int(input("Ingrese el radio de un círculo cualquiera: "))
area = (radio**2)*3.14
perimetro = 2*3.14*radio
print(f"Area: {area} Perímetro: {perimetro}")

#Ejercicio 5
segundos = int(input("Ingrese una cartidad de segundos para calcularla en horas: "))
horas = segundos // 3600
print(f"{segundos} segundos equivalen a {horas} horas")

#Ejercicio 6
num = int(input("Ingrese un número para calcular su tabla de multiplicar: "))
print(num," X 0 = ",num*0)
print(num," X 1 = ",num*1)
print(num," X 2 = ",num*2)
print(num," X 3 = ",num*3)
print(num," X 4 = ",num*4)
print(num," X 5 = ",num*5)
print(num," X 6 = ",num*6)
print(num," X 7 = ",num*7)
print(num," X 8 = ",num*8)
print(num," X 9 = ",num*9)
print(num," X 10 = ",num*10)

#Ejercicio 7
num1, num2 = int(input("Ingrese un número distinto de 0: ")), int(input("Ingrese otro número distinto de 0: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"La suma entre ambos números es: {suma} la resta entre ambos números es: {resta} la multiplicación entre ambos números es: {multiplicacion} la división entre ambos números es: {division}")

#Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura**2)
print(f"Su índice de masa corporal es igual a: {imc}")

#Ejercicio 9
grados_celsius = float(input("Ingrese la temperatura actual en grados celsius: "))
grados_fahrenheit = (grados_celsius*9/5)+32
print(f"La temperatura actual en grados Fahrenheit es: {grados_fahrenheit}")

#Ejercicio 10
num1, num2 = int(input("Ingrese un número entero por favor: ")), int(input("Ingrese otro número para calcular el promedio entre ambos: "))
promedio = (num1 + num2)/2
print(f"El promedio entre ambos números es de: {promedio}")
