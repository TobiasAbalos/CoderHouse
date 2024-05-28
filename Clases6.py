# esta_lloviendo = input('Esta lloviendo? ')

# if esta_lloviendo == 'si':
#     print('Entonces voy a usar paraguas cuando salga')
# else:
#     print('Entonces salgo sin paraguas')

# esta_lloviendo = input('Esta lloviendo? ').lower()

# if esta_lloviendo == 'si':
#     print('Entonces voy a usar paraguas cuando salga')
# elif esta_lloviendo == 'no':
#     print('Entonces no voy a usar paraguas')
# else:
#     print('No entiendo que me queres decir con eso')

# primer_numero = 30
# if primer_numero < 20:
#     print('es menor a 20')
# elif primer_numero < 30:
#     print('Es menor a 30')
# elif primer_numero < 40:
#     print('Es menor a 40')
# elif primer_numero < 50:
#     print('Es menor a 50')

# esta_lloviendo = input('Esta lloviendo? ').lower()
# pepito = ''
# pepito = 'Soy pepito' if esta_lloviendo == 'si' else ('No soy pepito')
# print(pepito)


preferencia = input('Ingrese su preferencia(Marvel/Capcom): ').capitalize()
nombre = input('Ingrese su nombre: ').upper()
if preferencia == 'Marvel' and nombre < 'M' or preferencia == 'CapCom' and nombre > 'N':
    print('Tu grupo es el A')
else:
    print('Tu grupo es el B')

