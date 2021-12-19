"""
Nessa aula, vamos aprender como funcionam os tipos primitivos no Python
e as peculiaridades do int() float() bool() e str().
Além disso, veremos como fazer as primeiras operações com a
função print() do Python.
"""
num_1 = input('Informe o primeiro numero: ')
num_2 = input('Informe o segundo numero: ')
num_1 = int(num_1)
num_2 = int(num_2)
result = num_1 + num_2
print(f'A soma de {num_1} + {num_2} e = {result}!')
