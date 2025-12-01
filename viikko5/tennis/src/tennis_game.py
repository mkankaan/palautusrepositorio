class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = [
            {"name": player1_name, "score": 0},
            {"name": player2_name, "score": 0},
        ]
        self.score_names = ["Love", "Fifteen", "Thirty", "Forty", "Deuce"]

    def won_point(self, player_name):
        for s in self.players:
            if s["name"] == player_name:
                s["score"] += 1

    def get_score(self):
        player1 = self.players[0]
        player2 = self.players[1]

        if self.tied(player1, player2):
            return self.deuce(player1["score"])
        elif self.is_winning(player1) or self.is_winning(player2):
            diff = abs(player1["score"]-player2["score"])
            leading_player = self.get_leading_player(player1, player2)

            if diff < 2:
                return self.advantage(leading_player)
            else:
                return self.win(leading_player)
        else:
            return "-".join([self.score_names[player1["score"]],
                             self.score_names[player2["score"]]])
    
    def deuce(self, score):
        return self.score_names[4] if score > 2 else self.score_names[score] + "-All"
    
    def get_leading_player(self, player1, player2):
        return player1 if player1["score"] > player2["score"] else player2
    
    def tied(self, player1, player2):
        return player1["score"] == player2["score"]
    
    def is_winning(self, player):
        return player["score"] > 3
    
    def advantage(self, player):
        return"Advantage " + player["name"]
    
    def win(self, player):
        return"Win for " + player["name"]
