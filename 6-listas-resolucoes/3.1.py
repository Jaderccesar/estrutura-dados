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
    
    def size1(self):
        # Complexidade assintotica O(n)
        count = 0
        walk = self.header.next
        while walk != self.trailer:
            count += 1
            walk = walk.next
        return count
    
llist = LinkedList()
llist.add_first('B')
llist.add_first('A')
llist.add_last('C')
llist.add_last('D')

print(llist.size1())