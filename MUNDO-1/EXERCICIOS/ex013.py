"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu
novo salário, com 15% de aumento.
"""

salario_atual = float(input('Informe o valor do Salário: R$'))
salario_aumento = salario_atual + (salario_atual * 15/100)
print(f'Salário Atual de R${salario_atual:.2f}\nSalário atualizado para R${salario_aumento:.2f}')
