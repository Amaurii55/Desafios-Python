'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''

n1 = float(input('Quantidade de reais na carteira: '))
dolar = n1 / 5.25 #Cotação do dolár US$ 1 = RS$ 5.25
print(f'Com RS${n1:.2f} você pode comprar US${dolar:.2f}')
