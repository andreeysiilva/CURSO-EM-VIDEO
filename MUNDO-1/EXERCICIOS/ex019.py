"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e
escrevendo na tela o nome do escolhido.
"""
from random import choice
aluno_1 = str(input('Digite o nome do 1º Aluno: '))
aluno_2 = str(input('Digite o nome do 2º Aluno: '))
aluno_3 = str(input('Digite o nome do 3º Aluno: '))
aluno_4 = str(input('Digite o nome do 4º Aluno: '))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
sorteio = choice(lista)
print(f'O aluno sorteado foi {sorteio}!!!')