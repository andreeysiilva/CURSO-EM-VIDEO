"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
"""

nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))
media = (nota_1 + nota_2) / 2
if media <= 5.0:
    print(f'Sua média é \033[1:32m{media}\033[m!!\nVocê foi \033[1:31mREPROVADO\033[m!!')
elif media <= 6.9:
    print(f'Sua média é \033[1:32m{media}\033[m!!\nVocê está de \033[1:33mRECUPERAÇÃO\033[m!!')
else:
    print(f'Sua média é \033[1:32m{media}\033[m\nVocê foi \033[1:34mAPROVADO\033[m!!')
