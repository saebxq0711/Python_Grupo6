import random

# Explicación del juego
print("Bienvenido a 'Adivina el número'!")
print("El objetivo del juego es adivinar un número secreto.")
print("Después de cada intento, recibirás una retroalimentación para ayudarte.")
print("¡Vamos a empezar!")

# Generar un número secreto aleatorio entre 1 y 20
numero_secreto = random.randint(1, 20)

# Solicitar la entrada del jugador
intentos = 0
adivinado = False

    
# Bucle principal del juego
while not adivinado:
    suposicion = input("Ingresa tu suposición (entre 1 y 20): ")
    
    # Validación de entrada
    if not suposicion.isdigit():
        print("Por favor, ingresa un número válido.")
        continue
    
    suposicion = int(suposicion)
    
    # Validación de rango
    if suposicion < 1 or suposicion > 20:
        print("El número debe estar en el rango de 1 a 20.")
        continue
    intentos += 1

    # Comparación y retroalimentación
    if suposicion < numero_secreto:
        print("Demasiado bajo. ¡Intenta nuevamente!")
    elif suposicion > numero_secreto:
        print("Demasiado alto. ¡Intenta nuevamente!")
    else:
        print(f"¡El número secreto era {suposicion}!")
        print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
        adivinado = True
        print(f"Intentos realizados: {intentos}")
        print("Gracias por jugar. ¡Hasta la próxima!")

