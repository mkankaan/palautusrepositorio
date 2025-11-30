class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

        self.scores = {player1_name: 0, player2_name: 0}
        self.score_names = ["Love", "Fifteen", "Thirty", "Forty", "Deuce"] #

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

        self.scores[player_name] += 1

    def get_score(self):
        p1_score = self.m_score1 #
        p2_score = self.m_score2 #

        if self.tied(self.scores[self.player1_name], self.scores[self.player2_name]):
            return self.deuce(self.m_score1)
        elif self.is_winning(self.scores[self.player1_name]) or self.is_winning(self.scores[self.player2_name]):
            minus_result = p1_score - p2_score
            #leading_player = self.get_leading_player()

            if minus_result == 1:
                return "Advantage player1"
            elif minus_result == -1:
                return "Advantage player2"
            elif minus_result >= 2:
                return "Win for player1"
            else:
                return "Win for player2"
        else:
            return "-".join([self.score_names[self.scores[self.player1_name]],
                             self.score_names[self.scores[self.player2_name]]])
    
    def deuce(self, score):
        return self.score_names[4] if score > 2 else self.score_names[score] + "-All"
    
    def get_leading_player(player1, player2):
        return player1 if player1["score"] > player2["score"] else player2
    
    def tied(self, player1_points, player2_points):
        return player1_points == player2_points
    
    def is_winning(self, score):
        return score > 3
