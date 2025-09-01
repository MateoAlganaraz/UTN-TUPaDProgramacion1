abecedario = "abcdefghijklmnñopqrstuvwxyz"

corrimiento = int(input("Cantidad de lugares que se correrán las letras: "))

mensajes_encriptados = []

for i in range(5):
    mensaje = input(f"Ingrese el mensaje: {i+1}: ")
    resultado = ""
    
    for letra in mensaje.lower(): 
        if letra in abecedario:
            indice = abecedario.index(letra)
            nuevo_indice = (indice + corrimiento) % 27
            resultado += abecedario[nuevo_indice]
        else:
            resultado += letra
    mensajes_encriptados.append(resultado)
    
print("\nmensajes encriptados: ")
for i in range(5):
    print(f"Oficial {i+1}: {mensajes_encriptados[i]}")