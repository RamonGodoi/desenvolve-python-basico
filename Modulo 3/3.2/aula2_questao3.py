idade=int(input("Qual sua idade? "))
jogos=input("Já jogou pelo menos 3 jogos de tabuleiro? ")
ganhou=int(input("Quantas vezes venceu um jogo? "))
idade_permitida=idade<=18 and idade>=16
quantidade_jogos= jogos=True
jogos_ganhos= ganhou>=1
apto=idade_permitida and quantidade_jogos and jogos_ganhos
print(f"Apto para ingressar no clube de jogos de tabuleiro:{apto}")
