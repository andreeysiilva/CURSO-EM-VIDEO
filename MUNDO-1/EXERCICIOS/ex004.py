"""
Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e todas
as informações possiveis sobre ele.
"""

dado = input('Digite um dado: ')
print(type(dado))
print('1',dado.isdigit())
print('2',dado.isnumeric())
print('3',dado.isalnum())
print('4',dado.isalpha())