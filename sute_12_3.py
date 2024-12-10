import unittest
from tests_12_3 import TournamentTest, TestClassRunner

test = unittest.TestSuite()
test.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
test.addTest(unittest.TestLoader().loadTestsFromTestCase(TestClassRunner))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test)
