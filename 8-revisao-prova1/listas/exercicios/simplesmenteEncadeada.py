class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

class ListaSimples:
    def __init__(self):
        self.head = None
    
    def inserirInicio(self, valor):
        novo = Node(valor)
        novo.next = self.head
        self.head = novo

    def __str__(self):
        elementos = []
        atual = self.head
        while atual:
            elementos.append(str(atual.element))
            atual = atual.next
        return " -> ".join(elementos)
    
lista = ListaSimples()
lista.inserirInicio('A')
lista.inserirInicio('B')
lista.inserirInicio('C')

print(lista)