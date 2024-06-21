while True:
    frase = input("Digite uma frase (ou 'Fim' para encerrar): ")
    if frase.lower() == 'fim':
        break
    frase_tratada = ''.join(c for c in frase if c.isalnum()).lower()
    if frase_tratada == frase_tratada[::-1]:
        print("A frase é um palíndromo!")
    else:
        print("A frase NÃO é um palíndromo.")
