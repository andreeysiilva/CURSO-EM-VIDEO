"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
data_atual = date.today().year

totmaior = 0
totmenor = 0
for pess in range(1, 8):
    ano = int(input(f'Informe o {pess}º ano de nascimento: '))
    maior = data_atual - ano
    if maior < 21:
        totmenor += 1
    else:
        totmaior += 1
print(f'{totmenor} não atingiram a maioridade!\n'
      f'{totmaior} atingiram a maioridade!')
