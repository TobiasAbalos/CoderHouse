# strings

# Metodo upper

#cadena1 = 'soY la pRimer cadena'
#print(cadena1)
#cadena1_en_mayusculas = cadena1.upper()
#print(cadena1)
#print(cadena1_en_mayusculas)

#cadena1_en_minisculas = cadena1.lower()
#print(cadena1_en_minisculas)

#cadena1_titulo = cadena1.title()
#print(cadena1_titulo)

#cadena1_parrafo = cadena1.capitalize()
#print(cadena1_parrafo)


# cadena1 = 'soY la pRimer cadena'
# print(cadena1.count('a'))
# print(cadena1.count(' '))
# print(cadena1.count('z'))

# print(cadena1.find('a'))
# print(cadena1.find(' '))
# print(cadena1.find(''))
# print(cadena1.find('z')) # No rompe, devuelve un negativo

# print(cadena1.rfind('a'))
# print(cadena1.rfind(' '))
# print(cadena1.rfind(''))
# print(cadena1.rfind('z')) # Busca de izquierda a derecha


# cadena2 = 'segunda cadena al rescate'
# # lista = ['segunda', 'cadena', 'al', 'rescate']
# lista = cadena2.split() # Desde un string cualquier recorta ese string en puntos
# print(lista)
# lista2 = cadena2.split('a')
# print(lista2)
# lista3 = cadena2.split('a ')
# print(lista3)
# lista4 = cadena2.split('asd el pepe loco')
# print(lista4)

# lista = ['segunda', 'cadena', 'al', 'rescate']
# # cadena = ' '.join(lista) JOIN se utiliza para unir elementos
# # print(cadena)
# cadena = ' ( (0).(0) ) '.join(lista)
# print(cadena)

# password = input('ingrese un password')


# palabra_repetida = 'cadena cadena cadena cadena cadena'
# palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra')
# palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra', 3)
# print(palabra_repetida)
# print(palabra_repetida_modificada)
# print(palabra_repetida.replace('cadena', 'otra', 3))
# Replace se utiliza para remplazar


# lista1 = ['primera', 'lista', 1]
# lista2 = ['segunda', 'lista', 2]
# # lista1 = []
# lista2.clear()
# print(lista1)
# print(lista2)

# lista = [1, 2, 3, 4]
# lista.insert(0, 65)
# print(lista)
# lista.extend('arigato')
# print(lista)

# lista.reverse()
# print(lista) # Da vuelta la lista


# lista_numeros = [5,1,2,3,4,10]
# lista_numeros.sort()
# # lista_numeros.sort(reverse=True) 
# print(lista_numeros)


# Dicts

# .copy crea una copia para que esta no modifique diferentes valores dentro de la memoria
# En listas/tuplas se puede utilizar .copy pero tambien [:]
# Ej: conjunto1 = {'lechuga', 'arroz'}
# conjunto2 = conjunto1.copy()
