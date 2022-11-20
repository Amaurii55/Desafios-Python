'''
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''

cel = float(input('Digite a temperatura em °C: '))
far = cel * 1.8 + 32
print(f'A temperatura em fahrenheit é de {far:.2f}°F')
