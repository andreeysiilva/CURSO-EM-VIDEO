"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.
"""

produto = float(input('Informe o valor do produto: R$'))
novo = produto - (produto * 5/100)
print(f'O Produto que custava R${produto:.2f}, na promoção de 5% vai custar R${novo:.2f}')
