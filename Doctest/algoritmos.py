'''
Created on 5 jun. 2020

@author: RSSpe
'''

def fibonacci(number):
    """
    El resultado debe de ser 144
    >>> fibonacci(12)
    144
    """
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonacci(number-1) + fibonacci(number-2)
    
def palindromo(sentence):
    """Retorna verdadero si el parametro es un palindromo
    en caso contrario retorna falso
    
    sentence -- String o entero
    
    >>> palindromo("oso")
    True
    
    >>> palindromo(12321)
    True
    
    >>> palindromo("CodigoFacilito")
    False
    """
    
    sentence = str(sentence).lower().replace(" ", "")
    return sentence == sentence[::-1]
    

import doctest
doctest.testmod()



