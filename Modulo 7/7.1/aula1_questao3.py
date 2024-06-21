def espacos(frase):
    contador=0
    for caractere in frase:
        if caractere==' ':
            contador+=1
    return contador
frase = input("Digite uma frase para contar os espaços em branco: ")
quantidade_espacos = espacos(frase)

print(f"A frase '{frase}' possui {quantidade_espacos} espaços em branco.")
