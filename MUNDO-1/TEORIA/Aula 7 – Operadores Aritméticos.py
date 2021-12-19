"""
Nessa aula, vamos aprender quais são os operadores aritméticos
do Python e também sua ordem de precedência dentro de expressões
matemáticas.
Veja como funcionam os operadores de adição, subtração,
multiplicação, divisão, exponenciação e quociente na linguagem Python.
"""

n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A Soma é {s}, o produto é {m:.2f} e a divisão é {d}.')
print(f'Divisão inteira é {di} e poténcia é {e}.')