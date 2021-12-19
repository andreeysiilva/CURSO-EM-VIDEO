"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
qtd_dias = int(input('Informe a quantidada de DIAS alugados: '))
qtd_km = float(input('Informe a quantidade de KM percorrido: '))
dia_fixo = qtd_dias * 60
km_fixo = qtd_km * 0.15
soma = km_fixo + dia_fixo
print(f'Valor total KM informados "{qtd_km}km" R${km_fixo:.2f}\nValor total DIAS informados "{qtd_dias}" R${dia_fixo:.2f}\nFatura total R${soma:.2f}')