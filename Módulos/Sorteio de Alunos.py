'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''

import random
nome1 = str(input('Escolha o primeiro nome: '))
nome2 = str(input('Escolha o segundo nome: '))
nome3 = str(input('Escolha o terceiro nome: '))
nome4 = str(input('Escolha o quarto e último nome: '))
escolhido = random.choice([nome1, nome2, nome3, nome4])  # Isto é uma lista, que é representada com [ ].
print(f'O aluno escolhido para apagar o quadro foi o(a) {escolhido}')
