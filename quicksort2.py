def quicksort(lista, inicio, fim):
    # se tiver mais de 2 elementos
    if inicio < fim:
        posicao = particionar(lista, inicio, fim)
        quicksort(lista, inicio, posicao-1)# pivotar a esquerda
        quicksort(lista, posicao+1, fim)# pivotar a direita

# preserva o pivo na sua posicao original até que eu detecte todos maiores e todos menores
def particionar(lista, inicio, fim):
    pivo = lista[inicio]# primeiro elemento da esquerda
    i = inicio # destino final do pivo
    j = inicio + 1 # contador para percorrer o restante da lista

    # percorrer o vetor
    while j <= fim:
        if lista[j] < pivo: # encontrei alguem menor
            i += 1 # encremento destino final do pivo
            trocar(lista, i, j)# trocar o elemento da posicao j pela posicao i
        j += 1 # passa para o proximo elemento

    trocar(lista, inicio, i) # colocar o pivo no seu destino

    return i

def trocar(lista, n, m):
    temp = lista[n]
    lista[n] = lista[m]
    lista[m] = temp

import random
import time

vetor = list(range(0, 5))
random.shuffle(vetor)

print(vetor)
antes = time.time()
quicksort(vetor, 0, len(vetor)-1)
depois = time.time()
total = (depois-antes)*1000

print(vetor)
print('O tempo total foi: %0.2f ms' % total)






