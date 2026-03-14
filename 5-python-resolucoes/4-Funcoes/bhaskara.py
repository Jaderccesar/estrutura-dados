import sys
import math

A = int(sys.argv[1])
B = int(sys.argv[2])
C = int(sys.argv[3])

delta = (B**2) - 4 * A * C

if delta < 0:
    print('A equacao nao possui numeros reais.')
else:
    x1 = (-B + (math.sqrt(delta))) / (2 * A)
    x2 = (-B - (math.sqrt(delta))) / (2 * A)

print(f'x1: {x1}, x2:{x2}')