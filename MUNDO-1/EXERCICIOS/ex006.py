"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e
raiz quadrada.
"""

num_1 = int(input('Informe um número: '))
dobro = num_1 * 2
triplo = num_1 * 3
raizq = num_1 ** (1/2)
print(f'O Dobro do Número "{num_1}" é {dobro}.\n O Triplo do Número "{num_1}" é {triplo}.\n A Raiz Quadrada do Número "{num_1}" é {raizq:.2f}.')