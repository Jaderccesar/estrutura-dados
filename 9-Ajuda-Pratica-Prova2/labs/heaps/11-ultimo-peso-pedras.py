'''
Estamos jogando um jogo com pedras. A cada turno, escolhemos as duas pedras mais pesadas e as
esmagantos juntas. Suponla que as pedras touhat pesos t e y com 2 € y. O resultado do esmagamento
ca se a = y, ambas as pedras são destruidase se 2 É U, a pedra de peso a é destruida e a pedra de peso y passa a ter peso 3 - 2. Ao final do jogo, testa no máximo uma pedra. Dados os pesos de um conjunto de pedras, retorne o peso da filtima pedra restante, ou 0 se não restar nenhuma pedra.
A entrada consiste nos pesos das pedras, representados por mimeros inteiros. Todos os pesos são apresentados em uma finica linha. A saida consiste cm rm nimero inteiro com a resultado.
Sua solução deve usar uma Ela de peloridade, esplorando a implementação baseada em árvores (heeps) fornecida pela biblioteca beupo. A solução deve ler um conjunto de casas de testo de um arquivo texto le.g., input.txti. com um caso de teste [pesos das pedras) por linha. O codigo deve ser executado
Lisando:
python lab-py < input,txt
Entrada
27 4181
Entrada
1
Saída
1
Saída
1
'''

# ============================================
# ÚLTIMA PEDRA
# USANDO HEAP (FILA DE PRIORIDADE)
# LEITURA VIA STDIN
# ============================================
#
# EXECUÇÃO:
#
# python lab.py < input.txt
#
# ============================================

import sys
import heapq


# --------------------------------------------
# PROCESSA UM CASO DE TESTE
# --------------------------------------------

def ultima_pedra(pedras):

    # heapq é MIN HEAP
    # usamos negativos para simular MAX HEAP

    heap = []

    for pedra in pedras:

        heapq.heappush(heap, -pedra)

    # enquanto houver pelo menos 2 pedras
    while len(heap) > 1:

        # duas maiores pedras
        x = -heapq.heappop(heap)
        y = -heapq.heappop(heap)

        # se diferentes
        if x != y:

            nova = abs(x - y)

            heapq.heappush(heap, -nova)

    # resultado final
    if len(heap) == 1:
        return -heap[0]

    return 0


# ============================================
# LEITURA DOS CASOS
# ============================================

for linha in sys.stdin:

    linha = linha.strip()

    # ignora linha vazia
    if linha == "":
        continue

    pedras = list(map(int, linha.split()))

    resultado = ultima_pedra(pedras)

    print(resultado)

# para rodar Get-Content .\input.txt | python .\11-ultimo-peso-pedras.py    