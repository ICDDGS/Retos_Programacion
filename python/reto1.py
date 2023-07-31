#!/usr/bin/env python
# coding: utf-8

# '''
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
# '''

# In[21]:


# Creación de un diccionario
leet = {
    #minusculas
    'a': '4',
    'b': '|3',
    'c': '[',
    'd': ')',
    'e': '3',
    'f': '|=',
    'g': '&',
    'h': '#',
    'i': '1',
    'j': ',_|',
    'k': '>|',
    'l': '1',
    'm': '^^',
    'n': '^/',
    'o': '0',
    'p': '|*',
    'q': '(_,)',
    'r': 'l2',
    's': '5',
    't': '7',
    'u': '(_)',
    'v': '\/',
    'w': 'vv',
    'x': '><',
    'y': 'j',
    'z': '2',
    #mayusculas
    'A': '4',
    'B': '|3',
    'C': '[',
    'D': ')',
    'E': '3',
    'F': '|=',
    'G': '&',
    'H': '#',
    'I': '1',
    'J': ',_|',
    'K': '>|',
    'L': '1',
    'M': '^^',
    'N': '^/',
    'O': '0',
    'P': '|*',
    'Q': '(_,)',
    'R': 'l2',
    'S': '5',
    'T': '7',
    'U': '(_)',
    'V': '\/',
    'W': 'vv',
    'X': '><',
    'Y': 'j',
    'Z': '2'
}



# In[22]:


def transformacion_LH(palabra):
    temp=""
    for i in range (0,len(palabra)):
        #print(leet[str(palabra[i])])
        temp=temp+leet[str(palabra[i])]
    return (temp)


# In[23]:


palabra = "prueba"
print(transformacion_LH(palabra))


# In[ ]:




