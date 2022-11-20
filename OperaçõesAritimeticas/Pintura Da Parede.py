'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede:'))
m2 = altura * largura
tinta = m2 / 2
print(f'A parede tem {m2} metros quadrados e será necessarios {tinta:.2f} litros de tinta para pintá-la')
