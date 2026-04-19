#Qual a complexidade assintotica no pior cawso (em termos de O) do algoritmo abaixo?

#Return the sum of the integers in given array

def alg1(arr):
    n = len(arr)
    total = 0
    for j in range(n):
        total += arr[j]
    return total

#R: A complixidade assintotica e O(N), complexidade linear, cresce conforme a entrada