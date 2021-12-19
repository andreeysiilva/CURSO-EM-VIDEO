"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
"""
print('{:#^40}'.format(' LOJA SILVA '))

preço_atual = float(input('Informe o valor do Produto: R$'))
print('')
print('ESCOLA A FORMA DE PAGAMENTO: \n'
      '[1] À vista dinheiro/cheque: \033[1:31m10% DE DESCONTO\033[m\n'
      '[2] À vista no cartão: \033[1:31m5% DE DESCONTO\033[m\n'
      '[3] 2x no cartão: \033[1:31mPreço Formal\033[m\n'
      '[4] 3x ou mais no cartão: \033[1:31m20% de juros\033[m')
opção = int(input('Selecione a opção: '))
print('')
if opção == 1:
      novo_preço = preço_atual - (preço_atual * 10 / 100)
      print(f'O produto que antes custava R$\033[1:31m{preço_atual:.2f}\033[m\n'
            f'Passou a custar R$\033[1:33m{novo_preço:.2f}\033[m')
elif opção == 2:
      novo_preço = preço_atual - (preço_atual * 5 / 100)
      print(f'O produto que antes custava R$\033[1:31m{preço_atual:.2f}\033[m\n'
            f'Passou a custar R$\033[1:33m{novo_preço:.2f}\033[m')
elif opção == 3:
      parcelas = preço_atual / 2
      print(f'Em 2x o valor de R$\033[1:31m{preço_atual:.2f}\033[m\n'
            f'Ficará em 2x de R$\033[1:33m{parcelas:.2f}\033[m \033[1:31mSEM JUROS\033[m!!')
elif opção == 4:
      parcelas = int(input('Em quantas parcelas? '))
      print('')
      novo_preço = preço_atual + (preço_atual * 20 / 100)
      parcela = novo_preço / parcelas
      print(f'Sua compra será parcelada em \033[1:31m{parcelas}\033[mx de R$\033[1:33m{parcela:.2f}\033[m COM JUROS!')
      print(f'O produto que antes custava R$\033[1:31m{preço_atual:.2f}\033[m\n'
            f'Passou a custar R$\033[1:33m{novo_preço:.2f}\033[m')
else:
      print('\033[1:31mOpção de pagamento inválida\033[m!!!')
