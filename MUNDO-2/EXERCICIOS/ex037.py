"""
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

numero = int(input('Informe um número inteiro: '))
print('Escolha uma Opção: ')
print('[1] \033[1:36mBINÁRIO\033[m\n[2] \033[1:33mOCTAL\033[m\n[3] \033[1:31mHEXADECIMAL\033[m')

selecao = str(input('Digite a opção que deseja converter: '))
if selecao == '1':
    binario = str(bin(numero))
    print(f'O número \033[1:36m{numero}\033[m convertido para \033[1:33mBinário\033[m é \033[1:31m{binario[2:]}\033[m')
elif selecao == '2':
    octal = str(oct(numero))
    print(f'O número \033[1:36m{numero}\033[m convertido para \033[1:33mOctal\033[m é \033[1:31m{octal[2:]}\033[m')
elif selecao == '3':
    hexa = str(hex(numero))
    print(f'O número \033[1:36m{numero}\033[m convertido para \033[1:33mHexadecimal\033[m é \033[1:31m{hexa[2:]}\033[m')
else:
    print('\033[1:31mOpção Inválida!!\033[m')