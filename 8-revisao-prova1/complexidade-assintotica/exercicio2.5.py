#Qual a complexidade assintotica no pior caso (em termos de O) do algoritmo abaixo?

#Returns the sum of the prefix sums of given array.
def alg3(arr):
    n = len(arr)
    total = 0
    for j in range(n):
        for k in range(j + 1):
            total += arr[k]
    return total

#R: O(n^2), complixidade quadrática, cresce muito