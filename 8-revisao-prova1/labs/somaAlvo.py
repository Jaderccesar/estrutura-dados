A = [2, 5, 2, 6, 1, 9, 2]

#Abordagem 1
def somaAlvo(array, T):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == T:
                print("A soma do indice ", i ," mais o indice ", j, " e igual a ", T)

#Abordagem 2
A.sort()
def somaAlvoOrdenado(array, T):
    tamanho = len(array)
    indiceInicial = 0
    indiceFinal = tamanho - 1
    while indiceInicial < indiceFinal:
        if array[indiceInicial] + array[indiceFinal] == T:
            print("A soma do indice ", indiceFinal ," mais o indice ", indiceInicial, " e igual a ", T)
        if array[indiceInicial] + array[indiceFinal] > T:
            indiceFinal -= 1
        else:
            indiceInicial += 1 
            
#somaAlvo(A, 7)
somaAlvoOrdenado(A, 7)

#R: Abordagem 1 tem complexidade O(n^2)
#R: Já a abordagem 2 tem complexidade O(n log n) por conta da ordenacao
#R: A abordagem 2 se torna mais vantajosa em vetores maiores, onde nao se precisa ler duas vezes o mesmo vetor