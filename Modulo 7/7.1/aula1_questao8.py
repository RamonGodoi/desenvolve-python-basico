def validar_cpf(cpf):
    cpf_numeros= ''.join(filter(str.isdigit, cpf))
    
    if cpf_numeros== cpf_numeros[0] * 11:
        return False
    soma= 0
    for i in range(9):
        soma+= int(cpf_numeros[i]) * (10 - i)
    resto= soma % 11
    if resto<2:
        digito_verif_1=0
    else:
        digito_verif_1=11-resto
    if digito_verif_1 != int(cpf_numeros[9]):
        return False
        soma = 0
    for i in range(10):
        soma += int(cpf_numeros[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito_verif_2=0
    else:
        digito_verif_2= 11 - resto
    if digito_verif_2 != int(cpf_numeros[10]):
        return False
    return True
cpf=input("Digite o CPF (XXX.XXX.XXX-XX): ")
if validar_cpf(cpf):
    print("CPF Válido")
else:
    print("CPF Inválido")
