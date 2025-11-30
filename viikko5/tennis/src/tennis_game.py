class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

        self.score_names = ["Love", "Fifteen", "Thirty", "Forty", "Deuce"] #

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        p1_score = self.m_score1 #
        p2_score = self.m_score2 #

        if p1_score == p2_score:
            return self.deuce(self.m_score1)
        elif p1_score >= 4 or p2_score >= 4:
            minus_result = p1_score - p2_score

            if minus_result == 1:
                return "Advantage player1"
            elif minus_result == -1:
                return "Advantage player2"
            elif minus_result >= 2:
                return "Win for player1"
            else:
                return "Win for player2"
        else:
            return "-".join([self.score_names[p1_score], self.score_names[p2_score]])
    
    def deuce(self, score):
        return self.score_names[4] if score > 2 else self.score_names[score] + "-All"
