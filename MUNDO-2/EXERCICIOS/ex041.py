"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""

from datetime import date
atual = date.today().year

ano = int(input('Informe o ano de nascimento: '))
idade = atual - ano
print(f'Sua idade é \033[1:31m{idade}\033[m.')

if idade <= 9:
    print('Sua categoria é \033[1:36mMIRIM\033[m!!')
elif idade <= 14:
    print('Sua categoria é \033[1:36mINFANTIL\033[m!!')
elif idade <= 19:
    print('Sua categoria é \033[1:36mJÚNIOR\033[m!!')
elif idade <= 25:
    print('Sua categoria é \033[1:36mSÊNIOR\033[m!!')
else:
    print('Sua categoria é \033[1:36mMASTER\033[m!!')