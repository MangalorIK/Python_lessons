import unittest


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
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.Usain = Runner('Усэйн', 10)
        self.Andrew = Runner('Андрей', 9)
        self.Nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        print([f"{key}: {value}" for key, value in self.all_results.items()], len(self.all_results))

    def testRun1(self):
        tournament = Tournament(90, self.Usain, self.Nick)
        self.all_results = tournament.start()
        self.tearDownClass()
        self.assertTrue(self.all_results[len(self.all_results)] == "Ник")

    def testRun2(self):
        tournament = Tournament(90, self.Andrew, self.Nick)
        self.all_results = tournament.start()
        self.tearDownClass()
        self.assertTrue(self.all_results[len(self.all_results)] == "Ник")

    def testRun3(self):
        tournament = Tournament(90, self.Usain, self.Andrew, self.Nick)
        self.all_results = tournament.start()
        self.tearDownClass()
        self.assertTrue(self.all_results[len(self.all_results)] == "Ник")

# if __name__ == '__main__':
#     unittest.main()
