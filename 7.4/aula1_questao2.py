import os
import re
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo_entrada = os.path.join(diretorio_script, "frase.txt")
caminho_arquivo_saida = os.path.join(diretorio_script, "palavras.txt")
if not os.path.exists(caminho_arquivo_entrada):
    print(f"O arquivo {caminho_arquivo_entrada} não foi encontrado.")
    exit()
with open(caminho_arquivo_entrada, 'r') as arquivo_entrada:
    frase = arquivo_entrada.read()
frase_processada = re.sub(r'[^a-zA-Z]', ' ', frase)
palavras = frase_processada.split()
with open(caminho_arquivo_saida, 'w') as arquivo_saida:
    for palavra in palavras:
        arquivo_saida.write(palavra + '\n')
with open(caminho_arquivo_saida, 'r') as arquivo_saida_leitura:
    conteudo_saida = arquivo_saida_leitura.read()

print("Conteúdo do arquivo 'palavras.txt':")
print(conteudo_saida)
