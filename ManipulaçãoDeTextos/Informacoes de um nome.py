'''
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite um nome: ')).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
total = len(nome) - nome.count(' ')
div = nome.split()
print(f'Fazendo a análise do nome...')
print(f'Seu nome em letras maiúsculas é {maiusculo}')
print(f'Seu nome em letras minúsculas é {minusculo}')
print(f'O total de letras no seu nome é {total}')
print(f'Seu primeiro nome é {(div[0])} e ele tem {len(div[0])} letras')

'''
Uma variação de 'Quantas letras tem o primeiro nome' pode ser a seguinte:

div = nome.find(' ')
print(f'O seu primeiro nome tem {div} letras')

# Simplismente buscou o espaço em branco após o primeiro nome, assim fazendo a contagem do espaço para trás.

'''