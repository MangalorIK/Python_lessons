import unittest
from runner_12_4 import Runner
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "test is frozen")
    def test_walk(self):
        try:
            nick = Runner("Nick", -5)
            for i in range(10):
                nick.walk()
            self.assertEqual(nick.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "test is frozen")
    def test_run(self):
        try:
            ben = Runner(68, 4)
            for i in range(10):
                ben.run()
            self.assertEqual(ben.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "test is frozen")
    def test_challenge(self):
        nick = Runner("Nick", 5)
        ben = Runner("Ben", 4)
        for i in range(10):
            ben.run()
            nick.walk()
        self.assertEqual(ben.distance == nick.distance, False)


if __name__ == '__main__':
    unittest.main()
