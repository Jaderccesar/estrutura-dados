class Node:
    def __init__(self, element, prev, next):
      self.element = element
      self.prev = prev
      self.next = next

class LinkedList:
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def __insert_between(self, e, predecessor, successor):
        newest = Node(e, predecessor, successor)
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest
    
    def __delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.element
        node.prev = node.next = node.element = None
        return element

    def first(self):
        if self.is_empty():
          raise Exception("List is empty")
        return self.header.next.element
    
    def last(self):
        if self.is_empty():
          raise Exception("List is empty")
        return self.trailer.prev.element
    
    def add_first(self, e):
        self.__insert_between(e, self.header, self.header.next)
    
    def add_last(self, e):
        self.__insert_between(e, self.trailer.prev, self.trailer)
    
    def remove_first(self):
        if self.is_empty():
          raise Exception("List is empty")
        return self.__delete_node(self.header.next)
    
    def remove_last(self):
        if self.is_empty():
          raise Exception("List is empty")
        return self.__delete_node(self.trailer.prev)

    def __str__(self):
        # Para imprimir a lista (print)
        answer = '( '
        walk = self.header.next
        while walk != self.trailer:
            answer += f'{walk.element} '
            walk = walk.next
        answer += ')'
        return answer
    
    def __str__(self):
        # Para imprimir a lista (print)
        answer = '( '
        walk = self.header.next
        while walk != self.trailer:
            answer += f'{walk.element} '
            walk = walk.next
        answer += ')'
        return answer
    
    def index(self, e):
        # Busca sequencial
        if self.is_empty(): return -1
        count = -1
        walk = self.header.next
        while walk != self.trailer:
            count += 1
            if walk.element == e:
                return count
            walk = walk.next
        return -1
    #Inicio Exercicio 3.1

    def size(self): 
        count = -1
        walk = self.header.next
        while walk != self.trailer:
            count += 1
            walk = walk.next
        return count
    #Complexidade O(n)
    #Fim Exercicio 3.1

    #Inicio Exercicio 3.2
    #Minha implementacao
    def centerNode(self):
        tamanho = -1
        contador = 0
        walk = self.header.next
        while walk != self.trailer:
            tamanho += 1
            walk = walk.next
        walk = self.header.next
        while contador < tamanho:
            contador += 1
            walk = walk.next
            if contador == int(tamanho / 2):
                return walk.element
        return -1
    #Complexidade O(n^2)
    #Implementacao correta
    def middle(self):
        inicio = self.header.next
        fim = self.trailer.prev
        while inicio != fim and inicio.next != fim:
            inicio = inicio.next
            fim = fim.prev
        return inicio
    #Complexidade O(n)
    #Fim exercicio 3.2
    #Inicio exercicio 3.3
    #Fim exercicio 3.3

llist = LinkedList()
llist.add_last('A')    
llist.add_last('B')    
llist.add_last('C')
llist.add_last('D')

llist2 = LinkedList()
llist2.add_last('E')    
llist2.add_last('F')    
llist2.add_last('G')
llist2.add_last('H')
               
#print(LinkedList.size(llist))   
#print(LinkedList.middle(llist))
#print(LinkedList.concatenarListas(llist, llist2))