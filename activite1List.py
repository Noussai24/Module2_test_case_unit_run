import unittest

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


if __name__ == '__main__':
    unittest.main()

# test Unitaire: test suite


class TestChainelist(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(chainelist([]), [])

    def test_single_element(self):
        self.assertEqual(chainelist([1]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(chainelist([1, 2, 2, 3, 3, 4, 5, 5]), [1, 2, 3, 4, 5])

    def test_mixed_types(self):
        self.assertEqual(chainelist(['a', 'b', 'b', 'c', 1, 1, 2, 2]), ['a', 'b', 'c', 1, 2])


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestChainelist('test_empty_list'))
    suite.addTest(TestChainelist('test_single_element'))
    suite.addTest(TestChainelist('test_duplicate_elements'))
    suite.addTest(TestChainelist('test_mixed_types'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
