'''
Created on 5 jun. 2020

@author: RSSpe
'''

import unittest
from shopping_cart import Item, ShoppingCart, NotExistItemError

class TestShoppingCart(unittest.TestCase):
    def setUp(self): # Este metodo se ejecuta antes de cada una de las pruebas unitarias
        self.pan = Item("Pan", 7.0)
        self.jugo = Item("Jugo", 5.0)
        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)
    
    def tearDown(self): # Este metodo se va a ejecutar despues de cada una de las pruebas unitarias
        pass
    
    def test_cinco_mas_cinco_igual_diez(self):
        assert 5 + 5 == 10
        
    def test_nombre_producto_igual_manzana(self):
        self.assertEqual(self.pan.name, "Pan") # assertEqual compara 2 valores y si son iguales pasa la prueba
        
    def test_nombre_producto_diferente_manzana(self):
        self.assertNotEqual(self.jugo.name, "Manzana") # assertNoEqual compara 2 valores y si son iguales la prueba falla

    def test_contiene_productos(self):
        self.assertTrue(self.shopping_cart.contains_item()) # assertTrue espera un valor verdadero
        
    def test_no_contiene_productos(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains_item()) # assertFalse espera un valor falso
        
    def test_obtener_producto_pan(self):
        item = self.shopping_cart.get_item(self.pan)
        self.assertIs(item, self.pan) # assertIs es para comparar si 2 objetos son el mismo
        self.assertIsNot(item, self.jugo)
        
    def test_exception_al_obtener_jugo(self):
        with self.assertRaises(NotExistItemError):
            self.shopping_cart.get_item(self.jugo)
            
    def test_total_con_un_producto(self):
        total =self.shopping_cart.total()
        self.assertGreater(total, 0) # assertGreater comprueba que sea mayor a un numero
        self.assertLess(total, self.pan.price + 1.0) # assertLess comprueba que sea menor a un numero
        # Hay otros asssert para mayor e igual, menor e igual
        self.assertEqual(total, self.pan.price)
        
    def test_codigo_pan(self):
        self.assertRegex(self.pan.code(), self.pan.name) # assertRegex ya implementa la libreria re y es para expresiones regulares
        
    def test_fail(self):
        """if 3 > 2:
            self.fail("2 no es mayor a 3")""" # Regularmente fail se ejecuta tras haber consultado una condicional, fail se ejecuta
            # para cuando los metodos assert de la clase TestCase no cubren lo que necesitan
            
    # Diferentes formas de saltarnos una prueba, es decir que no se ejecute:
    # 1.- Cuando el desarrollador conoce que una prueba no puede ejecutarse
    # 2.- Cuando el desarrollador desconoce si la prueba puede o no puede ejecutar debido a factores externos
    
    # Caso 1
    #@unittest.skip("Es una prueba") # Para saltarnos una prueba debemos de decorar el metodo y a skip debemos de pasarle un argumento que sea un String que sera la razon por la que se salto
    # Caso 2
    #@unittest.skipIf(True, "Es una prueba") # Para saltarnos una prueba debemos de decorar el metodo y a skip debemos de pasarle 2 argumentos, un valor booleano(si es verdadero se lo salta y caso contrario se ejecuta, e incluso podemos poner una comparacion) y otro argumento que sea un String que sera la razon por la que se salto
    @unittest.skipUnless(False, "Es una prueba") # Asi evaluamos a falso y tambien podemos poner una comparacion e igual colocamos un mensaje
    def test_prueba_skip(self):
        pass


if __name__ == '__main__':
    unittest.main()
