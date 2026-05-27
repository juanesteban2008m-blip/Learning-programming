import os
from random import randint

# ...............
# NUMERICS RACE
# ...............
os.system("clear")

#..............................
# VALIDAR NUMERO DE JUGADORES
#..............................
while True:
    num_players = int(input("ingrese la cantidad de jugadores (2-4):"))
    if num_players >= 2 and num_players <= 4:
        break 
    else:
        print("cantidad de jugadores no valida, vuelva a intentarlo")

#....................
# MENU DE NIVELES 
#....................
print("\n-----NIVELES-----")
print("\nNivel básico ( 20 posiciones)")
print("1. Nivel intermedio (30 posiciones)")
print("2. Nivel intermedio (30 posiciones)")
print("3. Nivel avanzado ( 50 posiciones)")
print("4. Nivel experto (100 posiciones)")

while True:
    level = int(input("Seleccione el nivel (1-4):"))
    if level >= 1 and level <= 4:
        break 
    else:
        print("nivel no valido, vuelva a intentarlo")

#........................
# VARIABLES DEL JUEGO
#.........................
posiciones = [0] * num_players 
dados_iguales = [0] * num_players
nivel_posiciones = [20, 30, 50, 100]
meta = nivel_posiciones[level - 1]
ganador = None

#...................
# INICIO DEL JUEGO
#...................

print("\n===== INICIA LA CARRERA =====")

while not ganador:

    for i in range(num_players):

        input(f"\nTurno del Jugador {i+1}. Presione ENTER para lanzar los dados...")

        dado1 = randint(1, 6)
        dado2 = randint(1, 6)

        print(f"Jugador {i+1} lanzó: {dado1} y {dado2}")

        # Avanzar posiciones
        movimiento = dado1 + dado2
        posiciones[i] += movimiento

        print(f"Avanza {movimiento} posiciones.")
        print(f"Posición actual: {posiciones[i]}")

        # =========================
        # VALIDAR DADOS IGUALES
        # =========================
        if dado1 == dado2:
            dados_iguales[i] += 1
            print(f"¡Dados iguales consecutivos!: {dados_iguales[i]}")
        else:
            dados_iguales[i] = 0

        # Gana si obtiene 3 pares consecutivos
        if dados_iguales[i] == 3:
            print(f"\n🏆 ¡Jugador {i+1} gana por obtener 3 dados iguales consecutivos!")
            ganador = True
            break

        # Gana si llega o supera la meta
        if posiciones[i] >= meta:
            print(f"\n🏆 ¡Jugador {i+1} ha llegado a la meta y gana la carrera!")
            ganador = True
            break