'''
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
'''
##Importaciones
import math

## Funcion creada para determinar si es primo un numero, de serlo se retornara un True de lo contrario False
def primo(numero):
    if numero == 2 :
        return True
    elif numero < 2 or numero % 2==0:
        return False
    else:
        for num in range (3, int(numero * 0.5)):
            if numero % num ==0:
                return False
        return True

## Funcion para determinar si pertenece a la serie de fibonacci, de serlo retornara True de lo contrario retornara False
def fibonacci(numero):
    if numero < 0:
        return False
    prueba1 = 5 * numero**2 + 4
    prueba2 = 5 * numero**2 - 4
    return cuadrado(prueba1) or cuadrado(prueba2)

## Funcion para determinar si es par, de serlo retornara True de lo contrario retornara false
def par(numero):
    if numero % 2 ==0: 
        return True
    else: 
        return False

## Funcion adiccional para realizar prueba de fibonacci, verifica que sea un cuadrado perfecto
def cuadrado(prueba):
    raiz_cuadrada = int(math.sqrt(prueba))
    return raiz_cuadrada**2 == prueba

## Funcion main encargada de armar el texto de salida que se mostrara al usuario
def main (numero):
    texto = 'El numero '+ str(numero)+': '
    if primo(numero):
        texto = texto + 'es primo, '
    else:
        texto = texto + 'no es primo, '
    if fibonacci(numero):
        texto = texto + 'pertenece a fibonacci, '
    else:
        texto = texto + 'no pertenece a fibonacci, '
    if par(numero):
        texto = texto + 'es par'
    else:
        texto = texto + 'no es par'
    
    print(texto)

## Llamada a la funcion main, se le debe dar el valor del numero que se comprobara
main(5)
