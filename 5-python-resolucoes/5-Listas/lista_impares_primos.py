vetImpar = [0] * 20
vetPrimo = [0] * 20
contador = 0
contadorPrimo = 0
ehPrimo = False
primo = 1
i = 1

while contador < 20 or contadorPrimo < 20:
    if not i % 2 == 0 and contador < 20:
        vetImpar[contador] = i
        contador += 1
    i += 1

    if contadorPrimo < 20:
        ehPrimo = True
    for i in range(2, primo-1):
        if primo % i == 0:
            ehPrimo = False
    if ehPrimo and primo >= 2:
        vetPrimo[contadorPrimo] = primo
        contadorPrimo += 1
    primo += 1
    
print(vetImpar)
print(vetPrimo)