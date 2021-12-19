"""
Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela a sua porção Inteira.
"""
from math import trunc

num_1 = float(input('Informe um número Real: '))
resultado = trunc(num_1)
print(f'O Valor digitado foi {num_1} é o seu valor inteiro é {resultado}.')