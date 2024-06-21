pares=[num for num in range(20, 51, 2)]
quadrados=[num ** 2 for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
divisiveis_por_7=[num for num in range(1, 101) if num % 7 == 0]
par_impar=["par" if num % 2 == 0 else "ímpar" for num in range(0, 30, 3)]
print("Todos os números pares entre 20 e 50:", pares)
print("Os quadrados de todos os valores de [1, 2, 3, 4, 5, 6, 7, 8, 9]:", quadrados)
print("Todos os números entre 1 e 100 que são divisíveis por 7:", divisiveis_por_7)
print("Para todos os valores em range(0, 30, 3), escreva 'par' ou 'ímpar':", par_impar)
