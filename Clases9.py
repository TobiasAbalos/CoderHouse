# def resta(num1, num2=20):
#    return num1, num2

# print(resta(1, 2))
# print(resta(num2=2, num1=1)) # Esto se puede hacer
# print(resta(num1=2, num2=1))
# print(resta(num2=2, 1)) No se puede porque el argumento esta antes
# print(resta(2, num1=1)) No se puede porque el valor 1 ya esta siendo utilizado

# print(resta(1))

# Se pueden poner valores en los argumentos en caso de querer hacer un ()
# Se pueden poner strings, False y True

# def saludo():
#     print(variable_prueba)
    
# variable_prueba = 'pepe' 
# Si la variable esta por debajo de saludo() no funciona
# saludo()

# def saludo():
#     print(variable_prueba)
    
# variable_prueba = 'Pepe' 

# saludo()

# def suma(*args):
#     print(type(args))
#     print(args)
    
# suma()

# *Args es una tupla y **Kwargs es un diccionario

def mostrar(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f'llave: {llave}')
    
mostrar(nombre= 'Pepito', apellido='Grillo')

# *Args posicion y **Kwargs por nombre