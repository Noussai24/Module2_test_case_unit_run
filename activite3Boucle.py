import unittest


from unittest.mock import patch


def nombreGrand():
    nombres = []  # j'initialise une liste vide pour enregistrer les nombres
    for i in range(3):  # on veut juste trois nombre
        nombre = int(input("Entrez le nombre : ")) 
        nombres.append(nombre)
    plus_grand_nombre = nombres[0]
    for elt in nombres:
        if elt > plus_grand_nombre:
            plus_grand_nombre = elt
    return plus_grand_nombre


resultat = nombreGrand()
print(f"Le plus grand nombre parmi les nombres saisis est :{resultat}") 
# affiche le nombre le plus grand

# Test Unitaire :


class TestNombreGrand(unittest.TestCase):
    @patch('builtins.input', side_effect=[5, 10, 3])
    def test_nombre_positif(self, mock_input):
        # Tester avec des nombres positifs
        self.assertEqual(nombreGrand(), 10)
 
    @patch('builtins.input', side_effect=[-2, 0, 5])
    def test_nombre_melange(self, mock_input):
        # Tester avec des nombres négatifs et positifs
        self.assertEqual(nombreGrand(), 5)  # Le plus grand nombre est 5
    
    @patch('builtins.input', side_effect=[-10, -5, -20])
    def test_nombre_negatifs(self, mock_input):
        # Tester avec des nombres négatifs uniquement
        self.assertEqual(nombreGrand(), -5)  # Le plus grand nombre est -5


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestNombreGrand('test_nombre_positif'))
    suite.addTest(TestNombreGrand('test_nombre_melange'))
    suite.addTest(TestNombreGrand('test_nombre_negatifs'))
    return suite


if __name__ == '__main__':
    unittest.main()