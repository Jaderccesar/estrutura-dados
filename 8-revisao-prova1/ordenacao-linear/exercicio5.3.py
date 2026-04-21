array = [8, 2, 6, 4, 8, 7, 1]
array2 = [5, 7, 4, 9, 8, 5, 6, 3]

def bubbleSort(array):
    n = len(array)
    for i in range (n):
        j = 0
        while j < n - 1:
                if array[j] >= array[j+1]:
                    valor = array[j]
                    array[j] = array[j+1]
                    array[j+1] = valor
                j += 1
    return array

print(bubbleSort(array2))

#Implementacao do professor

def bubble_sort(array):
     for last_index in range(len(array) - 1, 0, -1):
          for index in range(last_index):
               if array[index] > array[index + 1]:
                    array[index], array[index + 1] = array[index + 1], array[index] #isso aqui e loucura

#Exercicio 5.4
#Qual a complexidade assintotica de tempo do bubble sort
#Exemplo de array com 5 posicoes
# 4, 3, 2, 1, 0, andou n -1
# index vai andar respectivamente o tamnho de n
# ou seja O(n^2)
#Ps: no melhor caso ele interrompe, entao pode se dizer que O(n) no melhor caso.
# #