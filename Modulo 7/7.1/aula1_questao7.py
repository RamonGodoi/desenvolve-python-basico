import random
chave = random.randint(1, 10)
nomes = [
    "Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"
]
nomes_criptografados = []

for frase in nomes:
    nomes = ''.join(chr(ord(c) + chave) if 33 <= ord(c) <= 126 else c for c in frase)
    nomes_criptografados.append(nomes)
print("Nomes criptografados:")
for nome in nomes_criptografados:
    print(nome)
print(f"Chave de criptografia: {chave}")
