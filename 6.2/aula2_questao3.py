import random
from collections import Counter
lista1=[random.randint(0, 50)for _ in range(20)]
lista2=[random.randint(0, 50)for _ in range(20)]
interseccao=list(set(lista1)& set(lista2))
interseccao.sort()
contagem_lista1=Counter(lista1)
contagem_lista2=Counter(lista2)
print("lista1 -", lista1)
print("lista2 -", lista2)
print("interseccao ordenada -", interseccao)
for elemento in interseccao:
    print(f"O elemento {elemento} aparece {contagem_lista1[elemento]} vezes em lista1 e {contagem_lista2[elemento]} vezes em lista2.")
