#Criação do primeiro produto
produto1=input("Qual o produto?")
preco1=float(input("Qual o preço do pruduto?"))
quantidade1=int(input("quantos produtos?"))

#Criação do segundo produto
produto2=input("Qual o produto?")
preco2=float(input("Qual o preço do pruduto?"))
quantidade2=int(input("quantos produtos?"))

#Criação do terceiro produto
produto3=input("Qual o produto?")
preco3=float(input("Qual o preço do pruduto?"))
quantidade3=int(input("quantos produtos?"))

#Processamento
valor1=preco1*quantidade1
valor2=preco2*quantidade2
valor3=preco3*quantidade3
valortotal=valor1+valor2+valor3

#Impressão de dados(saída)
print(f"O valor total vai ser R${valortotal:,.2f}")