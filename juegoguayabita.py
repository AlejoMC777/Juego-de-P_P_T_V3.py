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


#Crear una función para que cada jugador lance el dado: Esta función llamará a la función lanzar_dado() y devolverá el resultado. Si el jugador saca 1 o 6, perderá su apuesta y se eliminará del juego.
def lanzar_jugador(jugador):
    resultado = lanzar_dado()
    print(f"{jugador['nombre']} ha sacado un {resultado}")
    if resultado == 1 or resultado == 6:
        print(f"{jugador['nombre']} ha perdido su apuesta de {jugador['apuesta']} (saldo actual: {jugador['saldo']})")
        jugador["eliminado"] = True
    elif resultado == 2 or resultado == 3:
        print(f"{jugador['nombre']} vuelve a lanzar...")
        lanzar_jugador(jugador)
    elif resultado == 4 or resultado == 5:
        print(f"{jugador['nombre']} pasa")
