"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%
"""
salario = float(input('Informe o valor do salário: R$'))

if salario <= 1250:
    salario_15 = salario + (salario * 15 / 100)
    print('Quem ganhava R${:.2f} passou a ganhar R${:.2f}'.format(salario, salario_15))
else:
    salario_10 = salario + (salario * 10 / 100)
    print('Quem ganhava R${:.2f} passou a ganhar R${:.2f}'.format(salario, salario_10))