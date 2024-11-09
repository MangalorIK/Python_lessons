import logging
import unittest
import runnerTest_12_4 as rt


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                        format="%(asctime)s | %(levelname)s | %(message)s ")
    logging.basicConfig(level=logging.WARNING, filemode="w", filename="runner_tests.log", encoding="utf-8",
                        format="%(asctime)s | %(levelname)s | %(message)s ")
    testSuite = unittest.TestSuite()
    testSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(rt.RunnerTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testSuite)
