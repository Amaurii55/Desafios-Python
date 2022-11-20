'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
Aula Anterior

'''

salario = float(input('Qual o seu salario atual?: '))
aumento = salario * 0.15
novosalario = salario + aumento
print(f'Com um aumento de 15% seu novo salario é de R${novosalario:.2f}')
