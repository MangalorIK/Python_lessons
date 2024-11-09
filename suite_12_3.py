import unittest
import module_12_2 as m2
import module_12_1 as m1

testSuite = unittest.TestSuite()
testSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(m1.RunnerTest))
testSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(m2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testSuite)