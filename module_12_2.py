from unittest import TestCase
from runner import Runner
from tournament import Tournament
class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.first = Runner('Усейн', 10)
        self.second = Runner('Андрей', 9)
        self.third = Runner('Ник',3)
