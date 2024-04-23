import unittest


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
