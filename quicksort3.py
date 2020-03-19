def quicksort(lista):
    if len(lista) > 1:
        menores = [x for x in lista[1:] if x < lista[0]]
        maiores = [x for x in lista[1:] if x > lista[0]]
        return (quicksort(menores) + [lista[0]] + quicksort(maiores))
    else:
        return lista

import random

vetor = list(range(0, 5))
random.shuffle(vetor)

print(vetor)
print(quicksort(vetor))






