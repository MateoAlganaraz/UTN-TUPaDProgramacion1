##Ejercicio 1
multiplos_4 = list(range(4, 101, 4)) #Comienza en 4, termina en 100, saltos de 4
print(multiplos_4)

##Ejercicio 2
mis_favoritas = ["pizza", "perro", "libros", "guitarra", "café"] 
print(mis_favoritas[-2]) #Índice -2 para que devuelva el penúltimo elemento

##Ejercicio 3
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print(lista_vacia)

##Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro" 
animales[-1] = "oso" #Reemplaza el último valor usando índice negativo
print(animales)

##Ejercicio 5
"""con max(numeros) buscamos el número más grande de la lista
y con el numeros.remove lo eliminamos
entonces la lista quedaría así: [8, 15, 3, 7]"""

##Ejercicio 6
lista_10_30 = list(range(10, 31, 5))
print(lista_10_30 [:2]) #Slicing para que solo muestre los dos primeros elementos 

##Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "pick-up"] #Reemplaza índices 1 y 2
print(autos)

##Ejercicio 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

##Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

##Ejercicio 10
lista_aninada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_aninada)
