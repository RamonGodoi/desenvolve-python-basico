genero=input("Qual seu genero? ")
idade=int(input("Qual sua idade? "))
tempo=int(input("Tem quantos anos de serviço? "))
a=(genero=="f" and idade>=60) or (genero=="m" and idade>=65)
b=tempo>30
c=idade>=60 and tempo>=25
pode_aposentar= a or b or c
print(pode_aposentar)