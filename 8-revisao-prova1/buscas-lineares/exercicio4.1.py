array = [4, 2, 66, 5, 7, 8, 1]
def buscaBinaria(array, busca):
    array.sort()
    for i in range(len(array)):
        if busca < array[i]:
            return "A busca: ", busca, " ultrapassou o valor: ", array[i] 
        if busca == array[i]:
            return "Encontrou o numero no indice: ", i

print(buscaBinaria(array, 1))