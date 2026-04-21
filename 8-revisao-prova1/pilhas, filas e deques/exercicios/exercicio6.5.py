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
    
    def transfer(S, T):
        while not S.is_empty():
            T.push(S.pop())
        return T
    
    
S = ArrayStack()
S.push('A')
S.push('B')
S.push('C')
S.push('D')
S.push('E')
T = ArrayStack()

print(ArrayStack.transfer(S, T))