import sys

x = int(sys.argv[11])
y = int(sys.argv[12])

vet = [0] * 10

for i in range(10):
    vet[i] = int(sys.argv[i + 1])

print(f'Soma: {vet[x - 1] + vet[y - 1]}')