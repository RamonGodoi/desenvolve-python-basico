def validador_senha(senha):
    if len(senha) <8:
        return False
    tem_maiuscula = False
    tem_minuscula = False
    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        if char.islower():
            tem_minuscula = True
        if tem_maiuscula and tem_minuscula:
            break
    if not (tem_maiuscula and tem_minuscula):
        return False
    tem_numero = any(char.isdigit() for char in senha)
    if not tem_numero:
        return False
    caracteres_especiais= set('@#$%&*!?.')
    tem_caractere_especial= any(char in caracteres_especiais for char in senha)
    if not tem_caractere_especial:
        return False
    return True

senha =input("Digite uma senha para validar: ")
if validador_senha(senha):
    print("A senha é válida!")
else:
    print("A senha inválida.")
   