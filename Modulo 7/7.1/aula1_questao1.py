def imprimir_escada_nome(nome):
    for i in range(1, len(nome) + 1):
        print(nome[:i])
nome=input("Digite seu nome: ")
imprimir_escada_nome(nome)
