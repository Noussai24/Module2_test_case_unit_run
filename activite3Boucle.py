import unittest


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
    def test_nombre_positif(self):
        # Tester avec des nombres positifs
        self.assertEqual(nombreGrand([5, 10, 3]), 10)
    
    def test_nombre_melange(self):
        # Tester avec des nombres négatifs et positifs
        self.assertEqual(nombreGrand([-2, 0, 5]), 5)
    
    def test_nombre_negatifs(self):
        # Tester avec des nombres négatifs uniquement
        self.assertEqual(nombreGrand([-10, -5, -20]), -5)


if __name__ == '__main__':
    unittest.main()