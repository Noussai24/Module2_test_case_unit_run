def nombreGrand():
    nombres = [] # j'initialise une liste vide pour enregistrer les nombres
    for i in range(3): # on veut juste trois nombre
        nombre = int(input("Entrez le nombre : ")) 
        nombres.append(nombre)
    plus_grand_nombre = nombres[0]
    for elt in nombres:
        if elt > plus_grand_nombre:
            plus_grand_nombre = elt
    return plus_grand_nombre


resultat=nombreGrand()
print(f"Le plus grand nombre parmi les nombres saisis est :{resultat}") 
# affiche le nombre le plus grand

class TestNombreGrandFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=[1, 7, 9])
    def test_nombre(self, mock_input):
        self.assertEqual(nombreGrand(),9)

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestNombreGrandFunction('test_nombre'))