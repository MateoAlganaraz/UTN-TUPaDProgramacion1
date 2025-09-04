ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input("Ingrese un número entre 1 y 17576000: "))

if 1 <= n <= 17576000:
    n -= 1  # ajustamos a base 0

    # Parte numérica
    numeros = n % 1000
    letras_valor = n // 1000

    # Parte de letras
    letras = ""
    for _ in range(3):
        resto = letras_valor % 26
        letras = ABC[resto] + letras
        letras_valor //= 26

    print(f"La patente correspondiente es: {letras} {numeros:03d}")
else:
    print("Número fuera de rango")
