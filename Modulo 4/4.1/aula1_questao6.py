n=int(input("número de experimentos: "))
cont=0
sapo, rato, coelho= 0, 0, 0
while cont<n:
    quantia=int(input())
    tipo=input()
    if tipo=="sapo": sapo+=quantia
    elif tipo=="rato": rato+=quantia
    elif tipo=="coelho": coelho+=quantia

    cont+=1

print(f"total de cobaias:{sapo+rato+coelho}")
print(f"total de sapos:{sapo} ")
print(f"total de ratos: {rato}")
print(f"total de coelhos: {coelho}")