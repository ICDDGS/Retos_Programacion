"""EL GENERADOR DE CONTRASEÑAS"""
"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
import random
import string

texto = "Hola Mundo 123"

# Contar la cantidad de letras en el texto
cantidad_letras = sum(caracter.isalpha() for caracter in texto)

def configurar_parametros():
    cantidad=0
    may='a'
    sim='a'
    num='a'
    while cantidad < 8 or cantidad>16:
        cantidad= int(input('Ingrese la cantidad de caracteres entre 8 y 16: '))

    while may!='y' and may!='n':
        may= input('¿Quiere incluir mayusculas? (y/n): ')

    while num!='y' and num!='n':
        num= input('¿Quiere incluir numeros? (y/n): ')
    
    while sim!='y' and sim!='n':
        sim= input('¿Quiere incluir simbolos? (y/n): ')
    generar_contrasena(cantidad,may,num,sim)

def generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    caracteres = string.ascii_lowercase  

    if incluir_mayusculas=='y':
        caracteres += string.ascii_uppercase

    if incluir_numeros=='y':
        caracteres += string.digits

    if incluir_simbolos=='y':
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    print(contrasena)

configurar_parametros()


