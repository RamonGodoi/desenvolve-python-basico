import random
lista=[random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)
inicio_intervalo=0
melhor_inicio=0
melhor_tamanho=0
while inicio_intervalo<len(lista):
    if lista[inicio_intervalo]<0:
        tamanho_intervalo=1
        while (inicio_intervalo+tamanho_intervalo)<len(lista) and lista[inicio_intervalo+tamanho_intervalo] < 0:
            tamanho_intervalo+=1
        if tamanho_intervalo>melhor_tamanho:
            melhor_inicio=inicio_intervalo
            melhor_tamanho=tamanho_intervalo
        inicio_intervalo+=tamanho_intervalo
    else:
        inicio_intervalo+=1
del lista[melhor_inicio:melhor_inicio + melhor_tamanho]
print("Editada:", lista)
