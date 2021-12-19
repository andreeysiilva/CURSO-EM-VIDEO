"""
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2m².
"""

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = largura * altura
qtd_tinta = area / 2
print(f'A Área total da parede é {area:.3f}m²\nÉ a quantidade de tinta utilizada é {qtd_tinta:.2f}L.')