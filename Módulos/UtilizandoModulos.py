'''
import (nome da biblioteca) Importa uma biblioteca para que suas funcões possam ser usadas
EX: import math

from (nome da biblioteca) import (função da biblioteca) Importa uma funcão específica da biblioteca
EX: from math import sqrt (raiz quadrada)
'''

# Este é um exemplo de importação de biblioteca onde toda a biblioteca será importada, disponibilizando todas as funcôes
# Sempre terá que usar math.(função) para especificar a função que deseja usar
# Ctrl + Espaço disponibiliza a lista de funções

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {raiz:.2f}')

# Pode ser utilizado math.ceil (para arredondar para cima) ou math.floor (para arredondar para baixo)
# Exemplo de importação de biblioteca onde apenas uma função foi importada (no caso a raiz (sqrt))
# Não precisa usar math.(função), pois ja foi definida a função desejada na importação
# Pode ser importado mais de uma função. Ex: from math import sqrt, floor

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz quadrada de {num} é {raiz:.2f}')
