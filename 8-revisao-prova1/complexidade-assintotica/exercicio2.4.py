#Qual a complexidade assintotica no pior caso (em termos de O) do algoritmo abaixo?

#Returns the sum of the integers with even index in given array

def alg2(arr):
    n = len(arr)
    total = 0
    for j in range(0, n, 2):
        total += arr[j]
    return total

#R: Seria um O(n/2) ou seja O(n), complexidade linear