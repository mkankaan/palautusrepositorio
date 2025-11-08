class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict["nationality"]
        self.team = dict["team"]
        self.goals = dict["goals"]
        self.assists = dict["assists"]

    
    def __str__(self):
        return f"{self.name:20} {self.team:20} {self.goals} + {self.assists} = {self.goals + self.assists}"

    def __eq__(self, other):
        return self.goals + self.assists == other.goals + other.assists

    def __lt__(self, other):
        return self.goals + self.assists < other.goals + other.assists
