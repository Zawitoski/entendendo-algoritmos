def quicksort(array):
    if len(array) < 2:
        return array
    else: 
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i >= pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
    
def simp_quicksort(array, inicio=0, fim=None):
    if fim is None:
        fim = len(array) - 1

    if inicio >= fim:
        return

    pivo = array[fim]
    i = inicio
    j = inicio

    # Particionamento manual
    while j < fim:
        if array[j] < pivo:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i += 1
        j += 1

    # Coloca o pivô no lugar certo
    temp = array[i]
    array[i] = array[fim]
    array[fim] = temp

    # Chamadas recursivas
    quicksort(array, inicio, i - 1)
    quicksort(array, i + 1, fim)

    return array


print(quicksort([10, 5, 2, 6, 7, 3]))