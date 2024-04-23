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


"""list = input("entrer une liste :").split()
result = chainelist(list)
print(f"votre liste unique est: {result}")"""

# Test Unitaire :


class TestChainelist(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(chainelist([]), [])

    def test_single_element(self):
        self.assertEqual(chainelist([1]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(chainelist([1, 2, 2, 3, 3, 4, 5, 5]), [1, 2, 3, 4, 5])

    def test_mixed_types(self):
        self.assertEqual(chainelist(['a', 'b', 'b', 'c', 1, 1, 2, 2]), ['a', 'b', 'c', 1, 2])


class TestRunnerList(unittest.TextTestRunner):
    def run(self, test):
        result = super().run(test)
        print(f"Total des TestRunnerList: {result.testsRun}, Erreurs:{len(result.errors)},Echecs:{len(result.failures)}")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestChainelist('test_empty_list'))
    suite.addTest(TestChainelist('test_single_element'))
    suite.addTest(TestChainelist('test_duplicate_elements'))
    suite.addTest(TestChainelist('test_mixed_types'))
    runner = TestRunnerList(verbosity=2)
    runner.run(suite)
