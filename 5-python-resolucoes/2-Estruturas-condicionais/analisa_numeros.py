primeiroNumero = input('Informe o primeiro numero: ')
segundoNumero  = input('Informe o sergundo numero: ')

if primeiroNumero > segundoNumero:
    print(F' O {primeiroNumero} e maior que o {segundoNumero}.')
elif primeiroNumero == segundoNumero:
    print(f' O {primeiroNumero} e o {segundoNumero} sao iguais.')
else:
    print(f'O {segundoNumero} e maior que o {primeiroNumero}.')