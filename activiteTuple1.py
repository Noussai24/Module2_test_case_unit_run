import unittest
import activite1Tuple


# Test case

class TestTupleCase(unittest.TestCase):
    def testlistvide(self):
        self.assertEqual(activite1Tuple.tupleplusgrand([]),())
# test Unitaire sur la liste


class TestTuple(unittest.TestCase):
    def testlistvide(self):
        self.assertEqual(activite1Tuple.tupleplusgrand([]),())
    
    def test_list_seul(self):
        self.assertEqual(activite1Tuple.tuple_plus_grand([(1,2,3)]),(1,2,3))
    
    def test_tuple_vide(self):
        self.assertEqual(activite1Tuple.tuple_plus_grand([(), (), ()]), ())
    
    def test_tuple_multiple(self):
        self.assertEqual(activite1Tuple.tuple_plus_grand([(1,), (2, 3), (4, 5, 6)]), (4, 5, 6))
    
    def test_tuple_double(self):
        self.assertEqual(activite1Tuple.tuple_plus_grand([(1, 2), (3, 4), (5, 6), (7, 8)]), (1, 2))


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
    runner = MyTestRunner(verbosity=2)
    runner.run(suite)