from random import randint
import os

# =========================
# CARRERA 
# =========================

# Función para limpiar pantalla
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


# =========================
# VALIDAR CANTIDAD DE JUGADORES
# =========================
while True:
    jugadores = int(input("Ingrese cantidad de jugadores (2 - 4): "))

    if 2 <= jugadores <= 4:
        break
    else:
        print("Error: Debe ingresar mínimo 2 y máximo 4 jugadores.")


# =========================
# MENÚ DE NIVELES
# =========================
print("\n===== NIVELES =====")
print("1. Nivel básico (20 posiciones)")
print("2. Nivel intermedio (30 posiciones)")
print("3. Nivel avanzado (50 posiciones)")
print("4. Nivel experto (100 posiciones)")


while True:
    nivel = int(input("\nSeleccione el nivel: "))

    if nivel == 1:
        meta = 20
        break
    elif nivel == 2:
        meta = 30
        break
    elif nivel == 3:
        meta = 50
        break
    elif nivel == 4:
        meta = 100
        break
    else:
        print("Nivel inválido. Intente nuevamente.")


# =========================
# VARIABLES DEL JUEGO
# =========================
posiciones = [0] * jugadores
dados_iguales = [0] * jugadores

ganador = False


# =========================
# INICIO DEL JUEGO
# =========================
print("\n===== INICIA LA CARRERA =====")

while not ganador:

    for i in range(jugadores):

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