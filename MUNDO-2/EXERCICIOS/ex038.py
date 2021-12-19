"""
Escreva um programa que leia dois números inteiros e compare-os.
Mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
"""

num_1 = int(input('Informe um número inteiro: '))
num_2 = int(input('Informe o segundo número inteiro: '))

if num_1 > num_2:
    print(f'O \033[1:31mPRIMEIRO\033[m valor e maior.')
elif num_2 > num_1:
    print(f'O \033[1:36mSEGUNDO\033[m valor é maior.')
else:
    print('Não existe valor maior, os dois são \033[1:35mIGUAIS\033[m.')
