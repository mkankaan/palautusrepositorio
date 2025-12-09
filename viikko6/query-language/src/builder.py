from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan

class Query:
    def __init__(self):
        self.matchers = []

    def build(self):
        return And(*self.matchers)

class QueryBuilder:
    def __init__(self, query = Query()):
        self.query = query

    def build(self):
        return self.query.build()
    
    def plays_in(self, team):
        self.query.matchers.append(PlaysIn(team))
        return QueryBuilder(self.query)
    
    def has_at_least(self, value, attr):
        self.query.matchers.append(HasAtLeast(value, attr))
        return QueryBuilder(self.query)
    
    def has_fewer_than(self, value, attr):
        self.query.matchers.append(HasFewerThan(value, attr))
        return QueryBuilder(self.query)
   
