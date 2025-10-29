import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),    # 4+12 = 16
            Player("Lemieux", "PIT", 45, 54),   # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53),   # 37+53 = 90
            Player("Yzerman", "DET", 42, 56),   # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)    # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_not_found(self):
        player = self.stats.search("Karri")
        self.assertEqual(player, None)

    def test_team(self):
        team = self.stats.team("EDM")
        names = ["Semenko", "Kurri", "Gretzky"]

        for i, player in enumerate(team):
            self.assertEqual(player.name, names[i])

    def test_top_default(self):
        top_names = ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]
        top_players = self.stats.top(4)

        for i, player in enumerate(top_players):
            self.assertEqual(player.name, top_names[i])

    def test_top_points(self):
        top_names = ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]
        top_players = self.stats.top(4, SortBy.POINTS)

        for i, player in enumerate(top_players):
            self.assertEqual(player.name, top_names[i])

    def test_top_goals(self):
        top_names = ["Lemieux", "Yzerman", "Kurri", "Gretzky", "Semenko"]
        top_players = self.stats.top(4, SortBy.GOALS)

        for i, player in enumerate(top_players):
            self.assertEqual(player.name, top_names[i])

    def test_top_assists(self):
        top_names = ["Gretzky", "Yzerman", "Lemieux", "Kurri", "Semenko"]
        top_players = self.stats.top(4, SortBy.ASSISTS)

        for i, player in enumerate(top_players):
            self.assertEqual(player.name, top_names[i])

    def test_top_invalid_enum_value(self):
        top_players = self.stats.top(4, 0)
        self.assertEqual(top_players, None)
