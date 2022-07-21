'''
Created on 5 jun. 2020

@author: RSSpe
'''

class Recursivo:
    """
    >>> recursivo = Recursivo()
    >>> recursivo.factorial(5)
    120"""
    def factorial(self, number):
        if number == 0: return 1
        else: return number * self.factorial(number - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # doctest.testfile("ruta del archivo") es para que ejecute pruebas de un archivo externo