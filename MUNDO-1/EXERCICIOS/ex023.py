"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada
um dos dígitos separados.
EX:
Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

num_1 = int(input('Informe um numero: '))
u = num_1 // 1 % 10
d = num_1 // 10 % 10
c = num_1 // 100 % 10
m = num_1 // 1000 % 10
print(f'Analisando o número: {num_1}')
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
