# move o pivô só no final
# agora tenho 2 sublistas, a da esquerda (menores), da direita (maiores)
# fazer quicksort em cima de cada uma delas

def quicksort(lista, inicio=0, fim=None):
    # faço isso por que vou precisar saber a posicao do pivô
    if fim is None:
        fim = len(lista)-1
    # somente se a lista tiver mais de 1 posicao
    if inicio < fim:
        pivo = partition(lista, inicio, fim)
        quicksort(lista, inicio, pivo-1) # para lista que fica a esquerda
        quicksort(lista, pivo+1, fim) # para lista que fica a direita

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return  i

