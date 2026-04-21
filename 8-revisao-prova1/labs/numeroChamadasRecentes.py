class Fila:
    def __init__(self):
        self.dados = []

    def enqueue(self, e):  # entra na fila
        self.dados.append(e)

    def dequeue(self):  # sai da fila
        if not self.is_empty():
            return self.dados.pop(0)

    def front(self):  # vê o primeiro
        if not self.is_empty():
            return self.dados[0]

    def is_empty(self):
        return len(self.dados) == 0

    def size(self):
        return len(self.dados)
    
    def ping(t):
        fila.enqueue(t)
        while fila.front() < (t- 3000):
            fila.dequeue()
        return fila.size()
         
fila = Fila()

print(Fila.ping(1))
print(Fila.ping(100))
print(Fila.ping(3001))
print(Fila.ping(3002))

