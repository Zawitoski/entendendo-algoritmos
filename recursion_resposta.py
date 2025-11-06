
def soma(lista):
    if lista == []:
        return 0
    return lista [0] + soma(lista[1:]) 

def conta(lista):
    if lista == []:
        return 0
    return 1 + conta(lista[1:])

def maior(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maior(lista[1:])
    return lista[0] if lista [0] > sub_max else sub_max

print('Soma = ' + str(soma([1,3,5,67,3,3,6])))
print('Conta = ' + str(conta([1,3,5,67,3,3,6])))
print('Maior = ' + str(maior([1,3,5,67,3,3,6])))

     