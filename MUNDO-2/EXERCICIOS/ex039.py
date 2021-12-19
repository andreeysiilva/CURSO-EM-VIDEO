"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

print('Informe o Sexo:\n[1] MASCULINO\n[2] FEMININO\n')
sexo = int(input('Digite sua opção: '))

if sexo == 1:
    nascimento = int(input('Informe o ano de nascimento: '))
    print('-=-' * 15)
    ano_atual = date.today().year
    idade = ano_atual - nascimento
    if idade == 18:
        print(f'Quem nasceu em \033[1:33m{nascimento}\033[m tem \033[1:32m{idade}\033[m.')
        print('E a hora \033[1:35mEXATA\033[m de se alistar!!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Quem nasceu em \033[1:33m{nascimento}\033[m tem \033[1:32m{idade}\033[m anos.')
        print(f'Ainda \033[1:36mFALTAM\033[m \033[1:31m{saldo}\033[m anos para se alistar!!')
        ano_futuro = ano_atual + saldo
        print(f'Seu ano de alistamento será em \033[1:31m{ano_futuro}\033[m')
    else:
        saldo = idade - 18
        print(f'Quem nasceu em \033[1:33m{nascimento}\033[m tem \033[1:32m{idade}\033[m anos.')
        print('Já \033[1:31mPASSOU\033[m do tempo do alistamento!!')
        print(f'Você deveria ter se alistado a \033[1:31m{saldo}\033[m anos atrás.')
        ano_passado = ano_atual - saldo
        print(f'O ano de alistamento foi em \033[1:31m{ano_passado}\033[m.')
elif sexo == 2:
    print('Não precisa fazer o alistamento obrigatório!!')
else:
    print('Essa opção não existe!!')
