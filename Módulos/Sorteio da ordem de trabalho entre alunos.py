'''
O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

from random import shuffle
nome1 = str(input('Escolha o primeiro nome: '))
nome2 = str(input('Escolha o segundo nome: '))
nome3 = str(input('Escolha o terceiro nome: '))
nome4 = str(input('Escolha o quarto e último nome: '))
ordem = [nome1, nome2, nome3, nome4]
shuffle(ordem)
print(f'A ordem escolhida foi {ordem}')
