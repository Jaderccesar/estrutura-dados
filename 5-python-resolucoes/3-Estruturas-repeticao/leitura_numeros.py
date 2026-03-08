numeroDigitado             = 1
quantidadeNumerosDigitados = 0
somaNumerosDigitados       = 0

while numeroDigitado != 0:
    numeroDigitado = int(input('Digite um numero: '))
    if numeroDigitado > 0:
        quantidadeNumerosDigitados += 1
        somaNumerosDigitados += numeroDigitado

mediaNumerosDigitados = somaNumerosDigitados / quantidadeNumerosDigitados

print(f'A quantidade de numeros digitados e {quantidadeNumerosDigitados}, a soma dos numeros digitados e {somaNumerosDigitados} e a media desses numeros e {format(mediaNumerosDigitados, '.2f')}')