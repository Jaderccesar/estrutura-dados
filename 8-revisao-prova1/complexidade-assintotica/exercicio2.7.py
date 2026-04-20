#Qual a complexidade assintotica no pior caso (em termos de O) do algoritmo abaixo?

#Returns the number of times second array stores sum of prefix sums from first.

def alg5(first, second):
    n = len(first)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(j + 1):
                total += first[k]
        if second[i] == total:
            count += 1
    return count

#R: O(n^3) complexidade cubica