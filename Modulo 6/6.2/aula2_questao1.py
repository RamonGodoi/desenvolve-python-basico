import random
valores = [random.randint(-100, 100) for _ in range(20)]
print("Lista original:", valores)
ordenados = sorted(valores)
print("Lista ordenada:", ordenados)
maior = valores.index(max(valores))
print("Índice do maior valor na lista original:", maior)
menor = valores.index(min(valores))
print("Índice do menor valor na lista original:", menor)
