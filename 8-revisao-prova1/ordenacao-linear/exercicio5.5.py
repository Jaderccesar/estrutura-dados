array = [8, 2, 6, 4, 8, 7, 1]
array2 = [1, 2, 4, 6, 7, 8, 10]

def arrayOrdenado(array):
    for i in range(len(array) - 1):
        if (array[i] > array[i + 1]):
            return "Array desordenado"
    return "Array ordenado corretamente"

print(arrayOrdenado(array))