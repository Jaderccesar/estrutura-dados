#Lab 2
# Considere um baralho ordenado de n cartas numeradas de 1 a n, com a carta 1 no topo do baralho e a carta n no 
# final. A seguinte operação é realizada enquanto houver pelo menos duas cartas no baralho:
# Joga fora (descarta) a carta do topo do baralho, e mova a nova carta do topo para o final do baralho.
# Sua tarefa é encontrar a sequência de cartas descartadas e a última carta restante. Para cada entrada 
# (número), o algoritmo deve produzir duas linhas de saída. A primeira linha apresenta a sequência de cartas
# descartas, enquanto a segunda linha mostra a última carta restante.

#Entrada: 7
#Saida: 
#discarded: 1, 3, 5, 7, 4, 2. 
#Remaining: 6

#Entrada: 19 
#Saida:
#Discarded: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 4, 8, 12, 16, 2, 10, 18, 14
#Remaining: 6

#Entrada: 10
#Saida:
#Discarded: 1, 3, 5, 7, 9, 2, 6, 10, 8
#Remaining: 4

#Meu passo a passo
#ter o baralho, pegar a carta do topo e remover, depois pegar a nova carta do topo e jogo pro final, tudo isso ate sobrar uma carta


def jogarCartasFora(n):
    baralho = criarBaralho(n)
    tamanho = len(baralho) - 1
    sobras = []
    contador = 0
    while len(baralho) > 1:
        sobras.append(baralho[0])
        baralho.remove(baralho[0])
        contador += 1
        baralho.insert(tamanho, baralho[0])
        baralho.remove(baralho[0])
        tamanho -= 1
    print('Discarded,', sobras)
    print('Ramaining: ', baralho)

def criarBaralho(n):
    baralho = [0] * n
    for i in range(n):
        baralho[i] = i + 1
    return baralho 

jogarCartasFora(19)