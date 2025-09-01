import random

victorias_jugador = 0
victorias_computadora = 0

while True:
    print("\nJuego: Piedra, Papel o Tijeras")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    #Validamos que elija una opción real
    if opcion not in ["1", "2", "3", "4"]:
        print("Opción inválida. Intenta de nuevo")
        continue
    
    #Probamos el break para evitar el bucle infinito
    if opcion == "4":
        print("\nJUEGO TERMINADO.")
        print(f"RESULTADO FINAL -> Jugador: {victorias_jugador} | Computadora: {victorias_computadora}")
        if victorias_jugador > victorias_computadora:
            print("Felicitaciones ganaste el juego!!!")
        elif victorias_computadora > victorias_jugador:
            print("Lo lamento has perdido. Vuelve a intentarlo!!")
        else: 
            print("El juego terminó en empate.")
        break
    
    #Declaramos e inicializamos las jugadas posibles y guardamos la jugada del usuario
    jugadas = ["Piedra", "Papel", "Tijera"]
    jugador = jugadas[int(opcion) - 1]
    
    #Guardamos la elección random de la computadora 
    computadora = random.choice(jugadas)
    
    print(f"\nJugador eligió: {jugador}")
    print(f"Computadora eligió: {computadora}")
    
    #Determinamos el ganador 
    if jugador == computadora:
        print("EMPATE")
    elif (jugador == "Piedra" and computadora == "Tijera") or \
        (jugador == "Tijera" and computadora == "Papel") or \
        (jugador == "Papel" and computadora == "Piedra"):
            print("Resultado: ¡JUGADOR GANA!")
            victorias_jugador += 1
    else:
        print("Resultado: Computadora gana")
        victorias_computadora += 1