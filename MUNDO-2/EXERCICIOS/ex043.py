"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
"""

peso = float(input('Informe o seu peso: (Kg)'))
altura = float(input('Informe a sua altura: (m)'))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é \033[1:31m{imc:.2f}\033[m')
if imc < 18.5:
    print('Você está \033[1:31mABAIXO DO PESO\033[m ideal!')
elif 18.5 <= imc < 25:
    print('Você está no \033[1:34mPESO\033[m ideal!')
elif 25 <= imc < 30:
    print('Você está \033[1:33mACIMA DO PESO\033[m ideal!')
elif 30 <= imc < 40:
    print('Você está com \033[1:31mOBESIDADE\033[m!')
else:
    print('Você está com \033[1:31mOBESIDADE MÓRBIDA\033[m!')
