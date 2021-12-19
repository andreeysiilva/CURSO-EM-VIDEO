"""
Crie um programa que leia quanto dinhero uma pessoa tem na
carteira e mostre quantos Dólares ela pode comprar.
Cotação Atual: 5,55
"""

carteira = float(input('Informe o valor em sua carteira: R$'))
dolar = carteira / 5.61
euro = carteira / 6.33
print(f'O Valor em sua Carteira é de R${carteira:.2f} Reais e pode comprar US${dolar:.2f} Doláres.\nOu\nPode comprar €{euro:.2f} Euros')
