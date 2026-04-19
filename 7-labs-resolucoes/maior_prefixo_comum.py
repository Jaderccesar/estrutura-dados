#Possivel resolucao

lista = ["flower", "flow", "fligth"]
lista2 = ["cadete", "cadetra", "cadetia"]

def maior_prefixo_comum(array):
    prefixo = array[0]
    retorno = ''

    for palavra in array[1:]:
        i = 0
        while i < len(palavra) and i < len(prefixo) and palavra[i] == prefixo[i]:
            i += 1
            retorno = prefixo[:i]
    return retorno