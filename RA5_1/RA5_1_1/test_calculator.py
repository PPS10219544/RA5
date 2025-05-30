import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()
        
    def test_multiplicar_enteros(self):
        self.assertEqual(self.calc.multiplicar(2, 3), 999)  # Provocamos error

    def test_multiplicar_flotantes(self):
        self.assertAlmostEqual(self.calc.multiplicar(2.5, 4.0), 10.0)

    def test_multiplicar_por_cero(self):
        self.assertEqual(self.calc.multiplicar(0, 100), 0)

if __name__ == '__main__':
    unittest.main()
