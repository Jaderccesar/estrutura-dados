# -*- coding: utf-8 -*-
"""
Arvore de Steiner em grafos.
- Leitura de instancias SteinLib (.stp)
- Heuristica TM (Takahashi-Matsuyama / caminho mais curto)
- Comparacao com KMB (nx.approximation.steiner_tree)
- Busca local de melhoria

Uso: coloque arquivos .stp na mesma pasta e rode:  python steiner.py
Sem .stp, roda uma instancia de demonstracao.
"""

#Este laboratório apresenta um estudo dirigido para a solução do problema da árvore de Steiner em grafos. Dado um grafo não dirigido ponderado G = (V,E) e um subconjunto de vértices I C V chamados terminais, deseja-se encontrar uma árvore de custo mínimo que conecte todos os vértices de T, podendo utilizar vértices adicionais (chamados vértices de Steiner) para reduzir o custo total. Esse problema tem aplicações em projeto de redes, como em telecomunicações, circuitos VLSI e redes de distribuição. O laboratório deve ser realizado seguindo os passos abaixo.
#1. Pesquisar sobre o problema da árvore de Steiner.
#2. Implementar uma função que faça a leitura das instâncias disponíveis em steinlib.zib.de e modele
#os grafos usando a biblioteca NetworkX.
#3. Pesquisar sobre a heurística de Takahashi-Matsuyama (TM), que constrói soluções para o problema.
#4. Implementar a heurística TM para resolver as instâncias escolhidas.
#5. Comparar o custo das soluções produzidas com aquelas retornadas pela heurística Kou-Markowitz-Berman (KMB), implementada em nx. algorithms.approximation.steiner_tree.
#6. Projetar uma etapa de melhoria das soluções construídas pela heurística TM, baseada em busca
#local (pesquisar).
#7. Comparar o desempenho do algoritmo final com a heurística KMB.

import glob
import networkx as nx
from networkx.algorithms.approximation import steiner_tree


# --------------------------------------------------- leitura SteinLib (.stp)
def ler_stp(caminho):
    G = nx.Graph()
    terminais = []
    with open(caminho, errors="ignore") as f:
        secao = None
        for linha in f:
            p = linha.split()
            if not p:
                continue
            chave = p[0].upper()
            if chave == "SECTION":
                secao = p[1].upper()
            elif chave == "END":
                secao = None
            elif chave == "E" and secao == "GRAPH":
                G.add_edge(int(p[1]), int(p[2]), weight=float(p[3]))
            elif chave == "T" and secao == "TERMINALS":
                terminais.append(int(p[1]))
    return G, terminais


def instancia_demo():
    G = nx.Graph()
    arestas = [(1,2,1),(2,3,1),(3,4,1),(1,5,5),(5,4,5),
               (2,6,2),(6,4,2),(1,4,10),(3,6,4)]
    for u, v, w in arestas:
        G.add_edge(u, v, weight=w)
    return G, [1, 3, 4]


# --------------------------------------------------- custo
def custo(T):
    return sum(d["weight"] for _, _, d in T.edges(data=True))


# --------------------------------------------------- heuristica TM
def takahashi_matsuyama(G, terminais):
    """Comeca por um terminal e conecta o terminal mais proximo por vez."""
    arvore_nos = {terminais[0]}
    T = nx.Graph()
    T.add_node(terminais[0])
    faltam = set(terminais[1:])
    while faltam:
        melhor = None  # (dist, caminho)
        for origem in arvore_nos:
            dist, cam = nx.single_source_dijkstra(G, origem, weight="weight")
            for t in faltam:
                if t in dist and (melhor is None or dist[t] < melhor[0]):
                    melhor = (dist[t], cam[t])
        caminho = melhor[1]
        for a, b in zip(caminho, caminho[1:]):
            T.add_edge(a, b, weight=G[a][b]["weight"])
            arvore_nos.add(b)
        faltam -= arvore_nos
    return podar(T, terminais)


# --------------------------------------------------- busca local / poda
def podar(T, terminais):
    """Remove folhas nao-terminais (nao contribuem para conectar terminais)."""
    T = T.copy()
    mudou = True
    while mudou:
        mudou = False
        for v in list(T.nodes):
            if v not in terminais and T.degree(v) == 1:
                T.remove_node(v)
                mudou = True
    return T


def busca_local(G, T, terminais):
    """Substitui a arvore pela MST do subgrafo induzido e poda folhas."""
    melhor = T
    melhor_c = custo(T)
    mudou = True
    while mudou:
        mudou = False
        nos = set(melhor.nodes)
        sub = G.subgraph(nos)
        if nx.is_connected(sub):
            mst = nx.minimum_spanning_tree(sub, weight="weight")
            mst = podar(mst, terminais)
            if custo(mst) < melhor_c:
                melhor, melhor_c = mst, custo(mst)
                mudou = True
    return melhor


# --------------------------------------------------- execucao
def resolver(nome, G, terminais):
    tm = takahashi_matsuyama(G, terminais)
    tm_bl = busca_local(G, tm, terminais)
    kmb = steiner_tree(G, terminais, weight="weight")
    print(f"\n===== {nome}  (|V|={G.number_of_nodes()}, "
          f"|E|={G.number_of_edges()}, terminais={len(terminais)}) =====")
    print(f"  TM              : {custo(tm):.1f}")
    print(f"  TM + busca local: {custo(tm_bl):.1f}")
    print(f"  KMB (networkx)  : {custo(kmb):.1f}")


def main():
    arquivos = sorted(glob.glob("*.stp"))
    if arquivos:
        for arq in arquivos:
            G, terminais = ler_stp(arq)
            resolver(arq, G, terminais)
    else:
        print(">> Nenhum .stp encontrado. Usando instancia de demonstracao.")
        G, terminais = instancia_demo()
        resolver("DEMO", G, terminais)


if __name__ == "__main__":
    main()

# ====================================================================
# 7) TM+busca local costuma igualar ou baixar o custo em relacao ao TM puro,
#    ficando proximo ou igual ao KMB. Ambas sao heuristicas: nenhuma garante
#    o otimo, mas dao solucoes boas em tempo polinomial.
# ====================================================================