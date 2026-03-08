import sys

numero = int(sys.argv[1])

contador = 0
divisor  = numero

while contador < 100:
    if divisor % numero == 0:
        print(divisor)
        contador += 1 
    divisor += 1