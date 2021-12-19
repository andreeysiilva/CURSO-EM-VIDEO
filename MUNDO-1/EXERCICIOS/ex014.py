"""
Escreva um programa que converta uma temperatura
digitando em graus Celsius e converta para graus Fahrenheit.
"""
temperatura = float(input('Informe a temperatura em ºC: '))
fahre = (temperatura * 9/5) + 32
print(f'Temperatura em Celsius {temperatura}ºC\nTemperatura em Fahrenheit {fahre}ºF')