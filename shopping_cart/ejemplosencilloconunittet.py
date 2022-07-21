'''
Created on 5 jun. 2020

@author: RSSpe
'''

import unittest
from shopping_cart import Item, ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self): # Este metodo se ejecuta antes de cada una de las pruebas unitarias
        print("Metodo setUp")
    
    def tearDown(self): # Este metodo se va a ejecutar despues de cada una de las pruebas unitarias
        print("Metodo tearDown")
    
    def test_cinco_mas_cinco_igual_diez(self):
        assert 5 + 5 == 10
        
    def test_nombre_producto_igual_manzana(self):
        item = Item("Manzana", 12.0)
        self.assertEqual(item.name, "Manzana", "El nombre no es manzana") # assertEqual compara 2 valores y si son iguales pasa la prueba

    def test_nombre_producto_diferente_manzana(self):
        item = Item("Pan blanco", 12.0)
        self.assertNotEqual(item.name, "Manzana", "El nombre es pan blanco") # assertNoEqual compara 2 valores y si son iguales la prueba falla


if __name__ == '__main__':
    unittest.main()