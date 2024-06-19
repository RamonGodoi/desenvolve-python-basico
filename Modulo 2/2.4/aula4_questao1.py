comprimento= int(input("Comprimento: ")) #Perguntar o comprimentro para calcular o m2
largura= int(input("Largura: ")) #Perguntar a largura para calcular o m2
preco_m2= float(input("valor do m2: ")) #Perguntar o preço do m2

area = comprimento*largura #calculo para definir o m2
preco_total = area*preco_m2 #calculo para definir o preço total

print(f"O terreno possui {area}m2 e custa R${preco_total:,.2f}")