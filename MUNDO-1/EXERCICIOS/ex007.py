"""
Desenvolva um programa que leia as duas notas de
um aluno, calcule e mostre a sua média.
"""

nota_1 = float(input('Informe a primeira Nota: '))
nota_2 = float(input('Informe a sugunda Nota: '))
nota_total = nota_2 + nota_1
nota_media = nota_total / 2
print(f'A soma das Notas são {nota_total:.1f} e a média das notas são {nota_media:.1f}.')