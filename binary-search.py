import random

# Página 27 - Ex: 1.1 - 1.2

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    iterations = 0

    while baixo <= alto:
        iterations += 1 
        
        meio = (alto + baixo) // 2
        chute = lista[meio]
        
        if chute == item:
            print("Found number, iterations =", iterations)
            return meio
        elif chute < item:
            baixo = meio + 1
        else:
            alto = meio - 1

    print("Didn't find number, iterations =", iterations)
    return None



def generate_sized_list(size):
    lista = [0] * size  
    numero = 0
    for number in range(size):
        numero += random.randint(1, 3)
        lista[number] = numero
    return lista

    
print("Number index = ", pesquisa_binaria(generate_sized_list(256), 9))
  