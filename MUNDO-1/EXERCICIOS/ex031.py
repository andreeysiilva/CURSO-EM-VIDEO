"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
200Km e R$0,45 para viagens mais longas.
"""

distancia = float(input('Informe a distancia da viagem: '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'A quantidade de km/h informados foi de {distancia:.2f}km/h\nO valor da viagem será de R${preço:.2f}.')