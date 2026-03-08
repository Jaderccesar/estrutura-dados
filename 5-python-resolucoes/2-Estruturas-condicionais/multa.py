velocidade = int(input('Qual a velocidade do carro: '))

if velocidade > 80:
    velocidade -= 80
    print(f'Voce foi multado em {velocidade * 30} R$.')