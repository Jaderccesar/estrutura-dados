import sys

class Pilha:
    def __init__(self):
        self.dados = []

    def push(self, e):
        self.dados.append(e)
    
    def pop(self):
        if not self.is_empty():
            return self.dados.pop()
        
    def top(self):
        if not self.is_empty():
            return self.dados[-1]
    
    def is_empty(self):
        return len(self.dados) == 0

    def size(self):
        return len(self.dados)

arrayOperacaoes = sys.argv

def placar(arrayOperacoes):
    pilha = Pilha()
    for op in arrayOperacaoes[1:]:
        if op.isdigit():
            pilha.push(int(op))

        if op == '+':
            A = pilha.pop()
            B = pilha.pop()
            pilha.push(B)
            pilha.push(A)
            pilha.push(A + B)    

        if op == 'D':
            pilha.push(pilha.top() * 2)

        if op == 'C':
            pilha.pop()
    return sum(pilha.dados)

print(placar(arrayOperacaoes))