import unittest 

def resta(a, b):
    return a - b

def sumas(a, b):
    return a + b

class testoperaciones(unittest.TestCase):
       def setup(self):
        pass

       def test_resta(self):
         esperado = 3
         actual = resta(5, 2)
        # Pásalo en el orden: actual, esperado
         self.assertEqual(actual, esperado)

       def test_suma(self):
         esperado = 1213
         actual = sumas(5, 7)
        # Pásalo en el orden: actual, esperado
         self.assertEqual(actual, esperado)



def tearDown(self):
   pass

if __name__ == '__main__':
    unittest.main()