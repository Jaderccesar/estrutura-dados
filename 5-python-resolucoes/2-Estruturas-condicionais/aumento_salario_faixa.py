import sys

salarioFuncionario = int(sys.argv[1])

if salarioFuncionario > 1250:
    aumentoSalarial = salarioFuncionario + salarioFuncionario * 0.10
else:
     aumentoSalarial = salarioFuncionario + salarioFuncionario * 0.15

print(f'O seu salario atual e: {aumentoSalarial}')