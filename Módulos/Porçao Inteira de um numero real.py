'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''

import math
num = float(input('Digite um número real: '))
int = math.trunc(num) # trunc mostra a parte inteira de um número
print(f'A parte inteira de {num} é {int}')
