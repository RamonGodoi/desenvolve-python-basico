def receber_lista(numero):
    print(f"Digite os {numero} elementos da lista {numero}:")
    lista = []
    for i in range(numero):
        elemento=int(input())
        lista.append(elemento)
    return lista
quantidade1=int(input("Digite a quantidade de elementos da lista 1: "))
lista1=receber_lista(quantidade1)
quantidade2=int(input("Digite a quantidade de elementos da lista 2: "))
lista2=receber_lista(quantidade2)
intercalada = []
i = 0
j = 0
while i < len(lista1) and j < len(lista2):
    intercalada.append(lista1[i])
    intercalada.append(lista2[j])
    i+=1
    j+=1
intercalada.extend(lista1[i:])
intercalada.extend(lista2[j:])
print("Lista intercalada:", intercalada)
