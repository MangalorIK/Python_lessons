import unittest
from pprint import pprint


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = Runner('Усэйн', 10)
        self.Andrew = Runner('Андрей', 9)
        self.Nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.items():
            print(i[1])

    def testRun1(self):
        self.tournament = Tournament(90, self.Usain, self.Nick)
        self.asserts()

    def testRun2(self):
        self.tournament = Tournament(90, self.Andrew, self.Nick)
        self.asserts()

    def testRun3(self):
        self.tournament = Tournament(90, self.Usain, self.Andrew, self.Nick)
        self.asserts()

    def asserts(self):
        self.results = self.tournament.start()
        self.assertTrue(self.results[len(self.results)] == "Ник")
        d = {k: v.name for k, v in self.results.items()}
        # print(d)
        self.all_results[len(self.all_results) + 1] = d

# if __name__ == '__main__':
#     unittest.main()
