def soma(lista, i=0):
    if i >= len(lista):
        return 0
    return lista[i] + soma(lista, i + 1)


def conta(lista, i=0):
    if i >= len(lista):
        return 0
    return 1 + conta(lista, i + 1)


def maior(lista, i=0, atual=None):
    if atual is None:
        atual = lista[0]

    if i >= len(lista):
        return atual

    if lista[i] > atual:
        atual = lista[i]

    return maior(lista, i + 1, atual)

print('Soma = ' + str(soma([1,3,5,67,3,3,6])))
print('Conta = ' + str(conta([1,3,5,67,3,3,6])))
print('Maior = ' + str(maior([1,3,5,67,3,3,6])))
