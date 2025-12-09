from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan

class Query:
    def __init__(self):
        self.matchers = []

    def build(self):
        return And(*self.matchers)
    
    def add_matcher(self, matcher):
        self.matchers.append(matcher)

class QueryBuilder:
    def __init__(self, query = Query()):
        self.query = query

    def build(self):
        return self.query
    
    def plays_in(self, team):
        self.query.add_matcher(PlaysIn(team))
        return self.query

