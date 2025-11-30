class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.scores = [
            {"name": player1_name, "score": 0},
            {"name": player2_name, "score": 0},
        ]
        self.score_names = ["Love", "Fifteen", "Thirty", "Forty", "Deuce"] #

    def won_point(self, player_name):
        for s in self.scores:
            if s["name"] == player_name:
                s["score"] += 1


    def get_score(self):
        if self.tied(self.scores[0]["score"], self.scores[1]["score"]):
            return self.deuce(self.scores[0]["score"])
        elif self.is_winning(self.scores[0]["score"]) or self.is_winning(self.scores[1]["score"]):
            diff = abs(self.scores[0]["score"]-self.scores[1]["score"])
            leading_player = self.get_leading_player(self.scores[0], self.scores[1])

            if diff < 2:
                return self.advantage(leading_player["name"])
            else:
                return self.win(leading_player["name"])
        else:
            return "-".join([self.score_names[self.scores[0]["score"]],
                             self.score_names[self.scores[1]["score"]]])
    
    def deuce(self, score):
        return self.score_names[4] if score > 2 else self.score_names[score] + "-All"
    
    def get_leading_player(self, player1, player2):
        return player1 if player1["score"] > player2["score"] else player2
    
    def tied(self, player1_score, player2_score):
        return player1_score == player2_score
    
    def is_winning(self, score):
        return score > 3
    
    def advantage(self, player_name):
        return"Advantage " + player_name
    
    def win(self, player_name):
        return"Win for " + player_name
