from paquete.modulo_solicitudes import *
from random import randint

def verificar_ganador_ronda(jugador, maquina):
    
    '''
    Determina quien gana la ronda.
    '''
    # 1 para Piedra, 2 para Papel, 3 para Tijera
    ganador=""
    if jugador == 1 and maquina == 3 or jugador == 2 and maquina == 1 or jugador == 3 and maquina == 2:
        ganador="jugador"
    elif maquina == 1 and jugador == 3 or maquina == 2 and jugador == 1 or maquina == 3 and jugador == 2:
        ganador = "maquina"
    else:
        ganador = "empate"
    return ganador

# -------------------------------------------------------------
def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):
    estado = True

    if aciertos_jugador == 2 or aciertos_maquina == 2:
        estado = False
    elif ronda_actual == 3:
        print("El juego continuará hasta que haya un ganador")

    return estado

# --------------------------------------------------------------

def verificar_ganador_partida(aciertos_jugador, aciertos_maquina):
    ganador=""
    if aciertos_jugador > aciertos_maquina:
        ganador="Gana el jugador por más puntos."
    else:
        ganador="Gana la maquina por más puntos."
    return ganador

#--------------------------------------------------------------- 

def mostrar_elemento(eleccion):
    elemento=""
    if eleccion == 1:
        elemento="Piedra"
    elif eleccion == 2:
        elemento="Papel"
    else:
        elemento="Tijera"
    return elemento

# ---------------------------------------------------------------

def jugar_piedra_papel_tijera():
    ronda = 1
    aciertos_jugador = 0
    aciertos_maquina = 0
    estado_partida = verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda)
    while estado_partida:
        jugador = preguntar_int_en_rango("Elija del 1 al 3: ", 1, 3)
        maquina = randint(1,3)
        ronda += 1
        ganador_ronda = verificar_ganador_ronda(jugador, maquina)
        if ganador_ronda == "jugador":
            aciertos_jugador += 1
        elif ganador_ronda == "maquina":
            aciertos_maquina += 1
        print(f"Jugador eligió: {mostrar_elemento(jugador)} - La máquina eligió: {mostrar_elemento(maquina)}")
        print(f"Aciertos jugador: {aciertos_jugador} - Aciertos maquina: {aciertos_maquina}")
        print("Ronda:",ronda)
        estado_partida = verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda)

    print(verificar_ganador_partida(aciertos_jugador, aciertos_maquina))

# print(verificar_ganador_ronda(jugador, maquina))
