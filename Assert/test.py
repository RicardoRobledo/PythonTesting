'''
Created on 5 jun. 2020

@author: RSSpe
'''

# Con pytest ponemos el siguiente comando en el simbolo del sistema: pytest "nombre del archivo".py

from algoritmos import fibonacci, palindromo, factorial

def test_fibonacci():
    assert fibonacci(5) == 5

def test_palindromo():
    assert palindromo("oso")
    
def test_factorial():
    assert factorial(5) == 120
    
