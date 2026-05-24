#Escreva um algoritmo recursivo que conta os nodos de uma árvore binária

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_node(root):
    if root is None:
        return 0
    
    return 1 + count_node(root.left) + count_node(root.right)

raiz = Node("A")

raiz.left = Node("B")
raiz.right = Node("C")

raiz.left.left = Node("D")
raiz.left.right = Node("E")

print(count_node(raiz))