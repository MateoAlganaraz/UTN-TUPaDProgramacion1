nombre = input("Nombre: ")
edad = int(input("Edad: "))
experiencia  = int(input("Años conduciendo: "))

if edad < 18:
    print("No puede conducir.")
elif edad >= 18 and experiencia  < 1:
    print("Principiante.")
elif edad >= 21 and experiencia  >= 1 and experiencia  <= 5:
    print("Conductor intermedio.")
elif edad >= 30 and experiencia > 10:
    print("Conductor profesional.")
else:
    print("Conductor estándar")