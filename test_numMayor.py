import unittest, math

from numMayor import *

class test_numMayor(unittest.TestCase):
    def test_numMaximo(self):
        numeroMaximo = numMaximo (23,43)
        self.assertEqual(numeroMaximo,43)

    def test_mayorEdad(self):
        mayEdad = mayorEdad(18)
        self.assertEqual(mayEdad,"Eres mayor de edad")
        
if  __name__== "main":
        unittest.main()

