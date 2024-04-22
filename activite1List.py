 
# Ennoncée et resolution
def chainelist(list):
    # creation d'une nouvelle list
    listFinal = []
    # parcourir la liste initiale
    for elt in list:
        # si l'element de la liste initial n'existe pas dans la nouvelle list
        if elt not in listFinal:
            # on ajoute l'element dans la nouvelle liste
            listFinal.append(elt)
    return listFinal


list = input("entrer une liste :").split()
result = chainelist(list)
print(f"votre liste unique est: {result}")


# test case
import unittest

def chainelist(lst):
    """ Crée une nouvelle liste sans doublons à partir de la liste donnée. """
    listFinal = []
    for elt in lst:
        if elt not in listFinal:
            listFinal.append(elt)
    return listFinal


class TestChainelistFunction(unittest.TestCase):
    """ Suite de tests pour vérifier la fonction chainelist. """

    def test_empty_list(self):
        """ Teste le fonctionnement avec une liste vide. """
        self.assertEqual(chainelist([]), [])

    def test_single_element(self):
        """ Teste une liste contenant un seul élément. """
        self.assertEqual(chainelist(['apple']), ['apple'])

    def test_no_duplicates(self):
        """ Teste une liste sans doublons initiaux. """
        self.assertEqual(chainelist(['1', '2', '3']), ['1', '2', '3'])

    def test_with_duplicates(self):
        """ Teste une liste avec des doublons. """
        self.assertEqual(chainelist(['1', '2', '2', '3', '1']), ['1', '2', '3'])

    def test_with_special_characters(self):
        """ Teste une liste contenant des caractères spéciaux. """
        self.assertEqual(chainelist(['@', '#', '@', '!']), ['@', '#', '!'])

    def test_case_sensitivity(self):
        """ Teste la sensibilité à la casse. """
        self.assertEqual(chainelist(['a', 'A', 'a']), ['a', 'A'])

    def test_with_non_string_elements(self):
        """ Teste une liste contenant différents types (int, str). """
        self.assertEqual(chainelist([1, '1', 2, '2']), [1, '1', 2, '2'])

if __name__ == '__main__':
    unittest.main()
