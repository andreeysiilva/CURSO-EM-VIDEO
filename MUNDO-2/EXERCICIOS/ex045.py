"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

import emoji
from random import randint
from time import sleep

pedra = emoji.emojize(":pedra:", language='pt') # EMOJI PEDRA
papel = emoji.emojize(":pergaminho:", language='pt') # EMOJI PAPEL
tesoura = emoji.emojize(":tesoura:", language='pt')# EMOJI TESOURA

# COMPUTADOR ESCOLHENDO AS ARMAS
itens = (f'\033[1;91m{pedra}\033[m', f'\033[1:33m{papel}\033[m', f'\033[1:36m{tesoura}\033[m')
computador = randint(0, 2)

# ESCOLHA DAS ARMAS
print("Escolha suas armas: \n"
      f"[0]\033[1;91m{pedra}\033[m"
      f" [1]\033[1:33m{papel}\033[m"
      f" [2]\033[1:36m{tesoura}\033[m")
jogador = int(input('Digite sua escolha: '))
if jogador != 0 and jogador != 1 and jogador !=2:
    print('JOGADA INVALIDA \nTENTE NOVAMENTE!!')
    quit()   # FAZ O PROGRAMA PARAR DE RODAR SOZINHO
else:
    print('-=' * 11)
    print('Jogador Jogou: {}'.format(itens[jogador]))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('Computador Jogou: {}'.format(itens[computador]))
    print('-=' * 11)
    # COMBATE
    if computador == 0: # COMPUTADOR JOGOU PEDRA
        if jogador == 0: # JOGADOR JOGOU PEDRA
            print(f'\033[1;91m{pedra}\033[m X \033[1;91m{pedra}\033[m = EMPATE!!!')
        elif jogador == 1: # JOGADOR JOGOU PAPEL
            print(f'\033[1;91m{pedra}\033[m X \033[1:33m{papel}\033[m = PAPEL ENCOBRE PEDRA, \033[1;91mJOGADOR VENCE!\033[m')
        elif jogador == 2: # JOGADOR JOGOU TESOURA
            print(f'\033[1;91m{pedra}\033[m X \033[1:36m{tesoura}\033[m = PEDRA AMASSA TESOURA, \033[1:33mCOMPUTADOR VENCE!\033[m')
        else:
            print('JOGADA INVÁLIDA!!')
    elif computador == 1: # COMPUTADOR JOGOU PAPEL
        if jogador == 0: # JOGADOR JOGOU PEDRA
            print(f'\033[1:33m{papel}\033[m X \033[1;91m{pedra}\033[m = PAPEL ENCOBRE PEDRA, \033[1:33mCOMPUTADOR VENCE!\033[m')
        elif jogador == 1: # JOGADOR JOGOU PAPEL
            print(f'\033[1:33m{papel}\033[m X \033[1:33m{papel}\033[m = EMPATE!!!')
        elif jogador == 2:# JOGADOR JOGOU TESOURA
            print(f'\033[1:33m{papel}\033[m X \033[1:36m{tesoura}\033[m = TESOURA CORTA PAPEL, \033[1;91mJOGADOR VENCE!\033[m')
        else:
            print('JOGADA INVÁLIDA!!')
    elif computador == 2: # COMPUTADOR JOGOU TESOURA
        if jogador == 0: # JOGADOR JOGOU PEDRA
            print(f'\033[1:36m{tesoura}\033[m X \033[1;91m{pedra}\033[m = PEDRA AMASSA TESOURA, \033[1;91mJOGADOR VENCE!\033[m')
        elif jogador == 1: # JOGADOR JOGOU PAPEL
            print(f'\033[1:36m{tesoura}\033[m X \033[1:33m{papel}\033[m = TESOURA CORTA PAPEL, \033[1:33mCOMPUTADOR VENCE!\033[m')
        elif jogador == 2: # JOGADOR JOGOU TESOURA
            print(f'\033[1:36m{tesoura}\033[m X \033[1:36m{tesoura}\033[m = EMPATE!!!')
        else:
            print('JOGADA INVÁLIDA!!')
    else:
        pass