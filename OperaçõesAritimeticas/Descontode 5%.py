'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

preço = float(input('Qual o preço do produto?: '))
desconto = preço * 0.05
ptotal = preço - desconto
print(f'O preço do produto com 5% de desconto é de R${ptotal:.2f}')
