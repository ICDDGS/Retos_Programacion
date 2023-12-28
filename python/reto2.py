'''
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
'''
P1=0
P2=0
secuencia = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
def puntuacion(puntaje):
    global P1,P2
    if puntaje== 'P1':
        P1 += 15
    elif puntaje == 'P2':
        P2 += 15

def score(resultados):
    for scr in resultados:
        puntuacion(scr)
        if P1 == P2:
            print('Deuce')
        elif P1 == 0:
            print('Love - ',P2)
        elif P2 == 0:
            print(P1,' - Love')
        else:
            print(P1,' - ',P2)
    ganador()

def ganador():
    if P1 > P2:
        print('El ganador es el P1')
    elif P2 > P1:
        print('El ganador es el P2')
    else:
        print('Deuce')

score(secuencia)