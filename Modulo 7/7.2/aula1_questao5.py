import random

def embaralhar_palavras(frase):
    palavras=frase.split()
    palavras_embaralhadas=[]
    for palavra in palavras:
        if len(palavra) <= 2:
            palavras_embaralhadas.append(palavra)
        else:
            primeira_letra=palavra[0]
            ultima_letra=palavra[-1]
            letras_internas= list(palavra[1:-1])
            random.shuffle(letras_internas)
            palavra_embaralhada= primeira_letra + ''.join(letras_internas) + ultima_letra
            palavras_embaralhadas.append(palavra_embaralhada)
    frase_embaralhada= ' '.join(palavras_embaralhadas)
    
    return frase_embaralhada

frase=input("Digite uma frase para embaralhar as palavras: ")
frase_embaralhada= embaralhar_palavras(frase)
print("Frase original:", frase)
print("Frase embaralhada:", frase_embaralhada)
