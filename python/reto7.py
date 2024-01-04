'''
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
'''
def preguntar(pregunta, opciones):
    print(pregunta)
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")
    respuesta = int(input("Selecciona tu respuesta (1-4): "))
    return respuesta - 1

def seleccionar_casa(respuestas):
    ambicion = respuestas[0]
    valentia = respuestas[1]
    lealtad = respuestas[2]
    inteligencia = respuestas[3]

    if valentia > 2 and ambicion < 2:
        return "Gryffindor"
    elif ambicion > 2 and inteligencia > 2:
        return "Slytherin"
    elif lealtad > 2:
        return "Hufflepuff"
    else:
        return "Ravenclaw"

def main():
    print("¡Bienvenido al sombrero seleccionador de Hogwarts!")
    
    preguntas = [
        "¿Qué cualidad valoras más en ti mismo?",
        "En una situación difícil, ¿qué harías?",
        "¿Qué tipo de amigo eres?",
        "¿Qué materia te resulta más interesante?",
        "¿Cuál es tu animal favorito?"
    ]

    opciones = [
        ["Valentía", "Ambición", "Lealtad", "Inteligencia"],
        ["Afrontarla con valentía", "Buscar la solución más astuta", "Pedir ayuda a un amigo", "Analizar la situación antes de actuar"],
        ["Lealtad y honestidad", "Astucia y ambición", "Empatía y amistad", "Intelecto y sabiduría"],
        ["Defensa contra las artes oscuras", "Pociones", "Cuidado de criaturas mágicas", "Adivinación"],
        ["León", "Serpiente", "Tejón", "Águila"]
    ]

    respuestas = []

    for i in range(5):
        respuesta = preguntar(preguntas[i], opciones[i])
        respuestas.append(respuesta)

    casa_seleccionada = seleccionar_casa(respuestas)

    print(f"\n¡El sombrero seleccionador ha decidido que perteneces a la casa de {casa_seleccionada}!")

if __name__ == "__main__":
    main()
