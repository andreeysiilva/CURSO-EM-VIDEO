"""
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle
aluno_1 = str(input('Informe o 1º Aluno: '))
aluno_2 = str(input('Informe o 2º Aluno: '))
aluno_3 = str(input('Informe o 3º Aluno: '))
aluno_4 = str(input('Informe o 4º Aluno: '))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)