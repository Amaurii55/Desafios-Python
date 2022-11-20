'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

import math
ang = float(input('Digite um ângulo: '))  #Fiz a conversão do ângulo para radianos.
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O seno do ângulo {ang} é {sen:.2f}')
print(f'O cosseno do ângulo {ang} é {cos:.2f}')
print(f'A tangente do ângulo {ang} é {tan:.2f}')
