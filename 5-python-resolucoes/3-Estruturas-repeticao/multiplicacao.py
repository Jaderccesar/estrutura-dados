import sys

numeroA = int(sys.argv[1])
numeroB = int(sys.argv[2])
resultado = 0

for i in range(numeroA):
    resultado += numeroB

print(f'A multiplicacao e: {resultado}')