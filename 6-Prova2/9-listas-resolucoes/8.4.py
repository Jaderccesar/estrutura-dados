class Name:
    def __init__(self):
        self.first = ""
        self.last = ""
    
    def set_name(self, first, last):
        self.first = first
        self.last = last

    def get_name(self):
        return str(self)
    
    def __str__(self):
        return f"{self.first} {self.last}"
    
    def __hash_(self):
        full_name = self.first + self.last

        hash_value = 0

        for char in full_name:
            hash_value += ord(char)
        
        return hash_value
    
p = Name()
p.set_name("Jader", "Vanderlinde")

print(p.__hash__())