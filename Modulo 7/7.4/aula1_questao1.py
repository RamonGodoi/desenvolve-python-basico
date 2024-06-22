import os
frase=input("Digite uma frase para salvar no arquivo 'frase.txt': ")
diretorio_script= os.path.dirname(os.path.abspath(__file__))
caminho_arquivo=os.path.join(diretorio_script, "frase.txt")
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write(frase)
print("Frase salva no arquivo:", caminho_arquivo)
