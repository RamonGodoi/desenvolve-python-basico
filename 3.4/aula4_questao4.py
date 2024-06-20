
distancia = float(input("Digite a distância da entrega em quilômetros: "))
peso = float(input("Digite o peso do pacote em quilogramas: "))
taxa_fixa = 0 
if distancia <= 100:
    valor_por_kg = 1
elif distancia <= 300:
    valor_por_kg = 1.5
else:
    valor_por_kg = 2

valor_frete = valor_por_kg * peso
if peso > 10:
    taxa_fixa = 10
valor_total = valor_frete + taxa_fixa

print(f"O valor do frete é R${valor_total:.2f}")
