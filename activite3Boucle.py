import unittest
from unittest.mock import patch


def nombreGrand():
    # j'initialise une liste vide pour enregistrer les nombres
    nombres = []
    # on veut juste trois nombre
    for i in range(3):
        nombre = int(input("Entrez le nombre : "))
        nombres.append(nombre)
    plus_grand_nombre = nombres[0]
    for elt in nombres:
        if elt > plus_grand_nombre:
            plus_grand_nombre = elt
    return plus_grand_nombre
# Test Unitaire: TestRunner


class TestNombreGrandFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=[1, 7, 9])
    def test_nombre_positif(self, mock_input):
        self.assertEqual(nombreGrand(),9)
    @patch('builtins.input', side_effect=[-3, -6, -7])
    def test_nombre_negatif(self, mock_input):
        self.assertEqual(nombreGrand(),-3)
    @patch('builtins.input', side_effect=[-3, 0, 6])
    def test_nombre_melange(self, mock_input):
        self.assertEqual(nombreGrand(), 6)


class MyTestRunner(unittest.TextTestRunner):
    def run(self, test):
        result = super().run(test)
        print(f"Total des tests: {result.testsRun}, Erreurs:{len(result.errors)},Echecs: {len(result.failures)}")
        return result
    

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestNombreGrandFunction('test_nombre'))
    suite.addTest(TestNombreGrandFunction('test_nombre_negatif'))
    suite.addTest(TestNombreGrandFunction('test_nombre_melange'))
    runner = MyTestRunner(verbosity=2)
    runner.run(suite)
