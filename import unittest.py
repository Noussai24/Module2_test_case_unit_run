import unittest


def tuple_plus_grand(list_tuples):
    # definir un tuple vide 
    plus_grand_tuple = ()
    max_elements = 0

    for tuple in list_tuples:
        if len(tuple) > max_elements:
            max_elements = len(tuple)
            plus_grand_tuple = tuple
    return plus_grand_tuple
# Test case


class TestTupleCase(unittest.TestCase):
    def testlistvide(self):
        self.assertEqual(tuple_plus_grand([]), ())
# test Unitaire sur la liste


class TestTuple(unittest.TestCase):
    def test_list_vide(self):
        self.assertEqual(tuple_plus_grand([]),())
    
    def test_list_seul(self):
        self.assertEqual(tuple_plus_grand([(1, 2, 3)]), (1, 2, 3))
    
    def test_tuple_vide(self):
        self.assertEqual(tuple_plus_grand([(), (), ()]), ())
    
    def test_tuple_multiple(self):
        self.assertEqual(tuple_plus_grand([(1,), (2, 3), (4, 5, 6)]), (4, 5, 6))
    
    def test_tuple_double(self):
        self.assertEqual(tuple_plus_grand([(1, 2), (3, 4), (5, 6), (7, 8)]), (1, 2))


class MyTestRunner(unittest.TextTestRunner):
    def run(self, test):
        result = super().run(test)
        print(f"Total des tests: {result.testsRun}, Erreurs:{len(result.errors)},Echecs: {len(result.failures)}")
        return result


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestTuple('test_list_vide'))
    suite.addTest(TestTuple('test_list_seul'))
    suite.addTest(TestTuple('test_tuple_vide'))
    suite.addTest(TestTuple('test_tuple_multiple'))
    suite.addTest(TestTuple('test_tuple_double'))