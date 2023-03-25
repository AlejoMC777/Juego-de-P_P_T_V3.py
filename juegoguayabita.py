#Crear una función para lanzar el dado: Esta función generará un número aleatorio entre 1 y 6 y lo devolverá como resultado.
import random

def lanzar_dado():
    return random.randint(1, 6)
#Crear una función para que cada jugador haga su apuesta: Esta función preguntará al jugador cuánto dinero desea apostar (debe ser mayor o igual a la apuesta mínima) y lo restará de su saldo. Si el jugador no tiene suficiente dinero para apostar, no podrá jugar y será eliminado del juego.

def hacer_apuesta(jugador, apuesta_minima):
    apuesta = int(input(f"{jugador}, ¿cuánto deseas apostar? (apuesta mínima: {apuesta_minima}): "))
    if apuesta < apuesta_minima or apuesta > jugador["saldo"]:
        print(f"No puedes apostar menos de {apuesta_minima} o más de {jugador['saldo']} (tu saldo actual)")
        return False
    else:
        jugador["saldo"] -= apuesta
        jugador["apuesta"] = apuesta
        print(f"{jugador['nombre']} ha apostado {apuesta} (saldo actual: {jugador['saldo']})")
        return True

