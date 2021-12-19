"""
Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo.
"""
from math import radians, sin, cos, tan
angulo = float(input('Informe o Angulo: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print(f'O Seno do Angulo {angulo:.1f}º é {seno:.2f}\nO Cosseno do Angulo {angulo:.1f}º é {coss:.2f}\nA Tangente do Angulo {angulo:.1f}º é {tang:.2f}')