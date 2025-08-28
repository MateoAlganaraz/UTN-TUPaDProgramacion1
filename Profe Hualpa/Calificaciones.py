from colorama import Fore, Style, init

init()

nombre = input("Nombre y apellido: ")
legajo = int(input("Legajo: "))
nota1 = int(input("Nota parcial 1: "))
nota2 = int(input("Nota parcial 2: "))
nota3 = int(input("Nota parcial 3: "))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10:
    print("Las notas deben estar entre 0 y 10")
    exit()

if nota1 < 4 or nota2 < 4 or nota3 < 4:
    resultado = Fore.RED+"Desaprobado (nota menor a 4)"+Style.RESET_ALL
    print(resultado)
    exit()

promedio = (nota1 + nota2 + nota3)/3

if promedio < 6:
    resultado = Fore.RED+"Desaprobado (promedio menor a 6)"+Style.RESET_ALL
elif promedio in (6,7,):
    resultado = Fore.YELLOW+"Aprobado con final"+Style.RESET_ALL
elif promedio >= 8:
    resultado = Fore.GREEN+"Promocionado"+Style.RESET_ALL

print("\n Resultado académico")
print(f"Alumno: {nombre}")
print(f"Legajo: {legajo}")
print(f"Notas: {nota1}+ {nota2}+ {nota3}")
print(f"Promedio: {promedio:.2f}")
print(f"Estado: {resultado}")
