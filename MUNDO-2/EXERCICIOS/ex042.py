"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""

reta_1 = float(input('Informe o valor da primeira reta: '))
reta_2 = float(input('Informe o valor da segunda reta: '))
reta_3 = float(input('Informe o valor da terceira reta: '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('Os segmentos acima \033[1:36mPODEM FORMAR\033[m um triângulo, ', end='')
    if reta_1 == reta_2 == reta_3:
        print('\033[1:32mEQUILÁTERO\033[m!!')
    elif reta_1 != reta_2 != reta_3 != reta_1:
        print('\033[1:33mESCALENO\033[m!!')
    else:
        print('\033[1:35mISÓSCELES\033[m!!')
else:
    print('Os segmentos acima \033[1:31mNÃO PODEM FORMAR\033[m triângulo!!')

