"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

casa = float(input('Informe o valor da casa: R$'))
salário_comprador = float(input('Informe o salário: R$'))
qtd_anos = int(input('Informe a quantidade de anos: '))

# Calculo VALOR CASA x ANOS
prestacao = casa / (qtd_anos * 12)

# Calculo dos 30% do salário do comprador
salario = salário_comprador * 30 / 100

print(f'Para pagar uma casa de R$\033[1:33m{casa:.2f}\033[m em \033[1:35m{qtd_anos}\033[m anos a parcela é de R$\033[1:31m{prestacao:.2f}\033[m')

if prestacao <= salario:
    print('Empréstimo \033[1:36mCONCEDIDO\033[m!')
else:
    print('Empréstimo \033[1:31mNEGADO\033[m!')
