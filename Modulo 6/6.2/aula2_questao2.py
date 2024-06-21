import random
num_elementos=random.randint(5, 20)
elementos=[random.randint(1, 10) for _ in range(num_elementos)]
print("Lista de elementos:", elementos)
soma=sum(elementos)
print("Soma dos elementos:", soma)
media=soma/num_elementos
print("Média dos elementos:", media)
