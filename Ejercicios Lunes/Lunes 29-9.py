import random

def elegir_palabra():
    palabras = ["messi", "aguero", "higuain", "mascherano", "otamendi", "fernandez", "alvarez", "paredes", "tagliafico", "montiel"]
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta])

def jugar_ahorcado():
    palabra_secreta = elegir_palabra()
    letras_adivinadas = []
    intentos = 6

    print("Juego del ahorcado con nombres de jugadores argentinos!")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    while intentos > 0:
        print("\nPalabra: ",mostrar_tablero(palabra_secreta, letras_adivinadas))
        print("Letras usadas: ", " ".join(sorted(letras_adivinadas)) if letras_adivinadas else "Ninguna por ahora.")
        
        letra = input("Adivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("Adivinaste una letra correctamente!")
        else:
            intentos -= 1
            print(f"Esta letra no se encuentra en la palabra, te quedan {intentos} intentos.")

        if all(l in letras_adivinadas for l in palabra_secreta):
            print("\n¡Felicidades! Adivinaste la palabra:", palabra_secreta)
            break

    else:
        print("\n¡Perdiste! La palabra era: ", palabra_secreta)

jugar_ahorcado()


