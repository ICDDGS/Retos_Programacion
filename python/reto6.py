'''
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
'''
'''
Caracterisitcas del juego:

* Piedra aplasta tijeras: La piedra gana contra las tijeras.
* Tijeras cortan papel: Las tijeras ganan contra el papel.
* Papel cubre a la piedra: El papel gana contra la piedra.
* Piedra aplasta lagarto: La piedra gana contra el lagarto.
* Lagarto envenena a Spock: El lagarto gana contra Spock.
* Spock rompe tijeras: Spock gana contra las tijeras.
* Tijeras decapitan lagarto: Las tijeras ganan contra el lagarto.
* Lagarto come papel: El lagarto gana contra el papel.
* Papel desaprueba a Spock: El papel gana contra Spock.
* Spock vaporiza la piedra: Spock gana contra la piedra.
'''

Player1=0
Player2=0
Entrada= [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]

def calculo_partidas(lista):
    global Player1
    global Player2
    for pares in lista:
        #Piedra
        if pares[0] =='🗿':
            if pares[1] == '✂️'or pares[1] =='🦎':
                Player1 += 1
            else:
                Player2 += 1
        
        #Tijeras
        if pares[0] =='✂️':
            if pares[1] == '📄'or pares[1] =='🦎':
                Player1 += 1
            else:
                Player2 += 1
        
        #papel
        if pares[0] =='📄':
            if pares[1] == '🗿'or pares[1] =='🖖':
                Player1 += 1
            else:
                Player2 += 1

        #lagarto
        if pares[0] =='🦎':
            if pares[1] == '🖖'or pares[1] =='📄':
                Player1 += 1
            else:
                Player2 += 1

        #spock
        if pares[0] =='🖖':
            if pares[1] == '✂️'or pares[1] =='🗿':
                Player1 += 1
            else:
                Player2 += 1
    puntaje()
    

def puntaje():
    global Player1, Player2
    print('Puntajes: ')
    print('Punataje Player1: ',Player1)
    print('Punataje Player2: ',Player2)

    if Player1>Player2:
        print('El ganador es el Player1')
    elif Player2>Player1:
        print('El ganador es el Player2')
    else:
        print('Tie (Empate) ')

    
calculo_partidas(Entrada) 