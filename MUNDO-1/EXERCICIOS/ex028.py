"""
Escreva um programa que faça o computador “pensar” em um número inteiro entre
0 e 5 e peça parao usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep
computador = randint(0, 5) # FAZ O COMPUTADOR GERAR UM NÚMERO RANDOMICO
print('-=-' * 17)
print('Vou pensar em um número entre 0 e 5 tente adivinhar')
print('-=-' * 17)
jogador = int(input('Em que número pensei? ')) # JOGADOR TENTA ADIVINHAR O NÚMERO
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me Vencer!')
else:
    print(f'GANHEI! Pensei no número {computador} e não no {jogador}!')
