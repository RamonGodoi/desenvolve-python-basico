frase=input("Escreva uma frase: ")
palavra_escolhida=input("Escreva a plavra: ")
objetivo=sorted(palavra_escolhida)
lst_palavras=frase.lower().split(" ")
for palavra in lst_palavras:
    if sorted(palavra) == objetivo:
        print(palavra)