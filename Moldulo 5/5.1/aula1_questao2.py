import random, math

n=int(input("Digite a quantidade de números inteiros: "))
soma=0
for i in range(n):
    valor=random.randint(0,100)
    soma+=valor
print("A raiz quadrada da soma é",math.sinh(soma))