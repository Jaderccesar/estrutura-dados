class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def get_first(self):
        return self.first
    
    def get_second(self):
        return self.second
    
    def __hash__(self):
        return hash(self.first) + hash(self.second)
    
    def __eq__(self, value):
        return self.first == value.first and self.second == value.secondW