#Ejercicio 1 "Bingo"
import random

def generar_carton():
    #random.sample(lista,k) toma 25 números random entre 1 y 50
    numeros = random.sample(range(1,51), 25) 
    #Slicing en la lista numeros. Con el [i:i+5] lo que hacemos es separar los 5 primeros elementos
    #gracias al for que tiene dentro este va desde 0 a 5. Y así con los siguientes, de 5 a 10, de 10 a 15 siempre sin incluir el stop
    #El resultado final es una lista de matrices (5x5)
    carton = [numeros[i:i+5] for i in range(0,21,5)]
    return carton

def mostrar_carton(carton):
    for fila in carton:
        #.join concatena en un solo string los elementos de una lista, separándolos en este caso por un espacio
        print(" ".join(f"{n:2}" for n in fila))
    print()
    
def hay_linea(carton):
    for fila in carton:
        if all(n==0 for n in fila):
            return True
    return False

def bingo(carton):
    return all(n==0 for fila in carton for n in fila)

def jugar_bingo():
    carton = generar_carton()
    print("Éste es tu cartón de bingo:")
    mostrar_carton(carton)
    
    #El set guarda cosas sin repetirlas en este caso sirve para no repetir número sorteados y evitar repetir el mensaje de linea completa
    numeros_sorteados = set()
    lineas_marcadas = set()
    
    while not bingo(carton):
        numero = random.randint(1,50)
        while numero in numeros_sorteados:
            numero = random.randint(1,50)
        numeros_sorteados.add(numero)
        
        print(f"Se sortea el número: {numero}")
    
        encontrado = False
        for i in range(5):
            for j in range(5):
                if carton[i][j] == numero:
                    carton[i][j] = 0
                    encontrado = True
                    
        if encontrado:
            print("NÚMERO ENCONTRADO EN EL CARTÓN!")
        else:
            print("No aparece en el cartón")
            
        mostrar_carton(carton)
        
        #Revisar líneas solo si no estaban marcadas antes, para que el mensaje de linea completada 
        #se muestre una vez cada vez que se completa una fila
        #enumerate() lo que hace es que recorre cualquier iterable y devuelve el índice y el valor
        for i,fila in enumerate(carton):
            if i not in lineas_marcadas and all(n==0 for n in fila):
                print("¡LINEA!")
                lineas_marcadas.add(i)
        
    print("¡BINGOOO!")
    
jugar_bingo()