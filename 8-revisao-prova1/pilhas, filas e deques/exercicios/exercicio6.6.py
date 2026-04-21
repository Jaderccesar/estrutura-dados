class ArrayStack:
    def __init__(self):
      self.data = []
      self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    
    def push(self, e):
        self.data.append(e)
        self.size += 1

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data[-1]
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        self.size -= 1
        return self.data.pop(-1)

    def __str__(self):
        # Para imprimir a pilha (print)
        content = '( '
        for element in self.data:
            content += element + ' '
        content += ')'
        return content
    
    def removeAll(pilha):
        if pilha.is_empty():
            return pilha
        while not pilha.is_empty():
            pilha.pop()
        return pilha
    
pilha = ArrayStack()
pilha.push('A')
pilha.push('B')
pilha.push('C')
pilha.push('D')
pilha.push('E')
pilha.push('F')
pilha.push('G')
pilha.push('H')

print(ArrayStack.removeAll(pilha))
