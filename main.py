import random

def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    print("¡Bienvenido a Piedra, Papel o Tijera!")
    
    usuario = input("Elige piedra, papel o tijera: ").lower()
    computadora = random.choice(opciones)
    
    print(f"La computadora eligió: {computadora}")
    
    if usuario == computadora:
        print("¡Es un empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and comNputadora == "papel"):
        print("¡Ganaste esta ronda!")
    else:
        print("¡Perdiste, gana la máquina!")

if __name__ == "__main__":
    piedra_papel_tijera()