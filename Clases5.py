# print(2+2)
# print(2*2)
# print(2-2)
# print(3/2)
# print(3**2)
# print(3//2)
# print(3%2)

# tipo de dato logico, son tipos de datos para sacar el verdadero o falso, esos datos son False y True (datos vuleanos)
#Tipo de datos logicos
# False (0)
# True(1)

#Casteado
# bool()

# print(True + 5)
# Operadores relacionales
# <> <= >= == !=(no igua)l
# = Es para asigacion

# print('B'<'a')
# print(ord('a')) ord sirve para saber la posicion en ascii
# chr()
# print(chr(97)) sirve para saber que letra esta en esa posicon

# print('ahorrar' < 'aHorrar')
# print('ah' < 'aHorrar')

# se puede usar con strings

# Se puede usar True o Flase para hacer operaciones
# print([False] == [0])

# print(bool(-4))

# expresiones = [
#     False == True,
#     10 >= 2*4,
#     33/3 == 11,
#     True > False,
#     True*5 == 2.5*2
# ]

# print(expresiones)

# Operadores Logicos "and or not"


nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))

resultado = nombre != '****' and 5 < edad < 20 and 4 >= len(nombre)  < 8 and edad * 3 > 35
print(resultado)
