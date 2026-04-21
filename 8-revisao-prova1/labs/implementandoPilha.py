class Pilha:
    def __init__(self):
        self.dados = []
    
    def push(self, e):
        self.dados.append(e)
    
    def pop(self, e):
        if not self.is_empty():
            return self.dados.pop
    
    def top(self):
        if not self.is_empty():
            return self.dados[-1]
        
    def is_empty(self):
        return len(self.dados) == 0

    def size(self):
        return len(self.dados)