# while [1,2,'pepe']:

# contador = 0
# while True:
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)

# contador = 0
# dato_de_condicion = True
# while dato_de_condicion > 0:
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)
#     dato_de_condicion -= 1

# contador = 0
# dato_de_condicion = True
# while dato_de_condicion:
#     if contador == 15:
#         dato_de_condicion = False
#     contador += 1
#     print('Estoy mostrando este mensaje numero:', contador)

# contador = 0
# dato_de_condicion = True
# while dato_de_condicion:
#     contador += 1
#     if contador == 15:
#         dato_de_condicion = False
    
#     print('Estoy mostrando este mensaje numero:', contador)

# if 2> 0:
#     ...

# contador = 0
# dato_de_condicion = 2
# while dato_de_condicion > 0:
#      contador += 1
#      print('Estoy mostrando este mensaje numero:', contador)
#      dato_de_condicion -= 1
# else:
#     print('Arroz')

# contador = 0
# while contador< 5:
#      contador += 1
#      if contador == 2:
#          continue
#      print('Estoy mostrando este mensaje numero:', contador)
# else:
#     print('Arroz')
    

# contador = 0
# while contador < 5:
#      contador += 1
#      if contador == 2:
#         break
#      print('Estoy mostrando este mensaje numero:', contador)
# else:
#     print('Arroz')
    
lista = [1,2,3,4, 'pepito', True, ('ee', 'aa')]
# print('La lista contiene el valor:', lista[0])
# print('La lista contiene el valor:', lista[1])

# indice = 0
# cant_de_elementos = len(lista)
# while indice < cant_de_elementos:
#     print('La lista contiene el valor:', lista[indice])
#     indice += 1
    
# for elemento in lista:
#     print('La lista contiene el valor:', elemento) 
    

# Enumerate
# range

lista = [1,2,3,4,5,6,7,8,9]

# for valor in lista:
#     print(valor * 2)
    
# rango = range(11)
# print(type(rango))
# lista_del_rango = list(rango)
# print(type(lista))

# for valor in lista_del_rango:
#     print(valor * 2)

# for valor in range(0,30, 3):
#     print(valor)

# cadena = 'Hola soy yo, vos quien sos?'
# indice = 0
# for letra in cadena:
#     print(letra)
    
# for indice, letra in enumerate(cadena):
#     print(f'La letra: {letra} ocupa el indice {indice}')