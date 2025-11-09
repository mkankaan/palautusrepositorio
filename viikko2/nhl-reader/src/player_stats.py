class PlayerStats:
    def __init__(self, player_reader):
        self._reader = player_reader
        self._players = self._reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        return sorted(filter(lambda p: p.nationality == nationality, self._players),
                      reverse=True)
