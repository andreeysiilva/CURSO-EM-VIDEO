"""
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

soma = 0
cont = 0
for m in range(1, 501, 2):
    if m % 3 == 0:
        cont += 1 # CONTADOR
        soma += m # ACUMULADOR
print(f'A quantidade de valores são {cont}.\n'
      f'A soma dos valores solicitados é {soma}.')
