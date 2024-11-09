import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "test is frozen")
    def test_walk(self):
        nick = Runner("Nick")
        for i in range(10):
            nick.walk()
        self.assertEqual(nick.distance, 50)

    @unittest.skipIf(is_frozen, "test is frozen")
    def test_run(self):
        ben = Runner("Ben")
        for i in range(10):
            ben.run()
        self.assertEqual(ben.distance, 100)

    @unittest.skipIf(is_frozen, "test is frozen")
    def test_challenge(self):
        nick = Runner("Nick")
        ben = Runner("Ben")
        for i in range(10):
            ben.run()
            nick.walk()
        self.assertEqual(ben.distance == nick.distance, False)


if __name__ == '__main__':
    unittest.main()