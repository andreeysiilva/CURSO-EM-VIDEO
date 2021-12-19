'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''

cate_opost = float(input('Informe o Cateto Oposto: '))
cate_adja = float(input('Informe o Cateto Adjacente: '))
hi = (cate_opost ** 2 + cate_adja ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')