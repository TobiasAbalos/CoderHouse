

# valor1 = int(input('ingresa un valor: '))
# valor2 = int(input('ingresa un valor: '))

# print(f'La suma de {valor1} y {valor2} es {valor1+valor2}')

import sys

print(sys.argv)

suma = 0
for valor in sys.argv[1:]:
    suma += int(valor)
    
print(f'La suma de {sys.argv[1:]} es {suma}')