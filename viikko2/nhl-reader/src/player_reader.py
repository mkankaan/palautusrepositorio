import requests
from player import Player

class PlayerReader():
    def __init__(self, url):
        self._url = url

    def get_players(self):
        url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
        response = requests.get(url).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players
