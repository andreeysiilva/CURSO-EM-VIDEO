"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadatamente.

EX: Ana Maria de Souza
primeiro: Ana
último: Souza
"""

nomec = str(input('Digite seu nome completo: ')).strip()
nome_lista = nomec.split()
print('Seu primeiro nome é {}'.format(nome_lista[0]))
print('Seu último nome é {}'.format(nome_lista[-1]))
