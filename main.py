import random

def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    
    intentos_usuario = 0
    intentos_computadora = 0

    print("Bienvenido a Piedra, Papel o Tijera")
    print("Tienes 3 intentos\n")

    for intento in range(1, 4):  
        print(f"\n--- Intento {intento} ---")
        
        usuario = input("Elige piedra, papel o tijera: ").lower()
        computadora = random.choice(opciones)
        
        print(f"La computadora eligió: {computadora}")
        
        if usuario == computadora:
            print("Empate, no suma puntos.")
        elif (usuario == "piedra" and computadora == "tijera") or \
            (usuario == "papel" and computadora == "piedra") or \
            (usuario == "tijera" and computadora == "papel"):
            print("¡Ganaste este intento!")
            intentos_usuario += 1
        else:
            print("Perdiste este intento.")
            intentos_computadora += 1


    print("\n--- RESULTADOS ---")
    print(f"Usuario ganó: {intentos_usuario} intentos")
    print(f"Computadora ganó: {intentos_computadora} intentos")

    if intentos_usuario > intentos_computadora:
        print(" Ganador definitivo: Usuario")
    elif intentos_computadora > intentos_usuario:
        print(" Ganador definitivo: Computadora")
    else:
        print(" Empate definitivo")

if __name__ == "__main__":
    piedra_papel_tijera()