"""
Crie um programa que leia um número inteiro e mostre na tela se ele é
PAR ou ÍMPAR.
"""

numero = int(input('Informe um numero inteiro: '))
resto = numero % 2
if resto == 0:
    print(f'O número {numero} é PAR')
else:
    print(f'O número {numero} é IMPAR')