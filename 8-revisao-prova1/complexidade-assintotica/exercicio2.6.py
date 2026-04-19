#Qual a complexidade assintotica no pior caso (em termos de O) do algoritmo abaixo?

#Returns the sum of the prefix sums of given array.

def alg4(arr):
    n = len(arr)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += arr[j]
        total += prefix
    return total

#R: Complexidade O(n), linear, cresce conforme a entrada