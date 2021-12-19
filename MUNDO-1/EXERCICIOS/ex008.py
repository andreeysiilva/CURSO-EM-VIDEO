"""
Escreva yn programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.
"""

metros = float(input("Informe a quantidade de Metros: "))
decâmetros = metros / 10
hectometro = metros / 100
km = metros / 1000
decimetros = metros * 10
centimetros = metros * 100
milimetros = metros * 1000
print(f'A quantidade de Metros informados foi "{metros:.1f}" convertidos em:\nDecâmetros: {decâmetros:.1f}dam\nHectómetro: {hectometro:.2f}hm\nKm: {km}km\nDecímetros: {decimetros:.2f}dm\nCentímetros: {centimetros:.2f}cm\nMilímetros: {milimetros:.2f}mm')