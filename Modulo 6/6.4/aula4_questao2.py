frase=input("Digite uma frase: ")
vogais="aeiouAEIOU"
lista_vogais=sorted([ch for ch in frase if ch in vogais])
lista_consoantes=[ch for ch in frase if ch.isalpha() and ch not in vogais]
print("Lista de vogais:", lista_vogais)
print("Lista de consoantes:", lista_consoantes)
