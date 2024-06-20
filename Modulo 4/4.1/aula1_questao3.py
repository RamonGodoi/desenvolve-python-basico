n1, n2, n3 = float(input()), float(input()), float(input())
m= (n1+n2+n3)/3
if m >= 60:
    print("Aprovado")
elif m>=40:
    print("Recuperação")
else:
    print("Reprovado")
print("Fim")