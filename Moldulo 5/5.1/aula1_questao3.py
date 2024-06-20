import random


numero=random.randint(1, 10)

while True:
    palpite = int(input("Tente adivinhar o número secreto (entre 1 e 10): "))
    if palpite < numero:
        print("Muito baixo. Tente novamente!")
    elif palpite > numero:
        print("Muito alto. Tente novamente!")
    else:
        print(f"Correto! O numero é {numero}!")
        break  
