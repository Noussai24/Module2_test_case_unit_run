# Importation des modules nécessaires pour le test
import unittest
from unittest.mock import patch

def nombreGrand():
    # Initialisation d'une liste vide stocker les nombres entrés l'utilisateur
    nombres = []  
    # Boucle pour obtenir exactement trois nombres de l'utilisateur
    for i in range(3):
        nombre = int(input("Entrez le nombre : "))  
        # Demande à l'utilisateur d'entrer un nombre
        nombres.append(nombre)  
        # Ajout du nombre entré à la liste des nombres
    plus_grand_nombre = nombres[0]  
    # Initialisation du plus grand nombre avec le premier élément de la liste
    # Boucle pour déterminer le plus grand nombre dans la liste
    for elt in nombres:
        if elt > plus_grand_nombre:
            plus_grand_nombre = elt  # Mise à jour du plus grand nombre si un nombre plus grand est trouvé
    return plus_grand_nombre  # Retour du plus grand nombre trouvé

# Exécution de la fonction et impression du résultat
resultat = nombreGrand()
print(f"Le plus grand nombre parmi les nombres saisis est : {resultat}")

# Définition de la classe de test pour la fonction nombreGrand
class TestNombreGrandFunction(unittest.TestCase):
    # Test de la fonction avec des entrées simulées
    @patch('builtins.input', side_effect=[1, 7, 9])  
    # Simulation de l'entrée utilisateur avec trois nombres
    def test_nombre(self, mock_input):
        self.assertEqual(nombreGrand(), 9)  
        # Vérification que la fonction retourne le plus grand nombre correctement

# Bloc principal pour exécuter les tests si ce script est exécuté comme programme principal
if __name__ == '__main__':
    suite = unittest.TestSuite()  # Création d'une suite de tests
    suite.addTest(TestNombreGrandFunction('test_nombre'))  # Ajout du test à la suite de tests
