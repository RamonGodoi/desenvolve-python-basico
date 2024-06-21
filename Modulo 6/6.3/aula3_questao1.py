def receber_lista():
    print("Digite uma quantidade indefinida de números inteiros (pelo menos 4 valores).")
    print("Para parar, digite 'fim'.")
    lista = []
    while True:
        entrada = input("Digite um número inteiro ou 'fim' para parar: ")
        if entrada.lower() == 'fim':
            break
        try:
            numero = int(entrada)
            lista.append(numero)
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    if len(lista) < 4:
        print("Você digitou menos de 4 valores. Execute o programa novamente.")
        return None
    else:
        return lista
lista=receber_lista()
if lista:
    print("Lista original:", lista)
    print("Os 3 primeiros elementos:", lista[:3])
    print("Os 2 últimos elementos:", lista[-2:])
    print("Lista invertida:", lista[::-1])
    print("Elementos de índice par:", lista[::2])
    print("Elementos de índice ímpar:", lista[1::2])
