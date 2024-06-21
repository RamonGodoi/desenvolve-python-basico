meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril','Maio', 'Junho', 'Julho', 'Agosto','Setembro', 'Outubro', 'Novembro', 'Dezembro']
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = data_nascimento.split('/')
mes_extenso = meses[int(mes) - 1]
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")
