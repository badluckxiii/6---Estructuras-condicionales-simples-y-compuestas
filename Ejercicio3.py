#  Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar 
# un mensaje indicando si el número tiene uno o dos dígitos.
# (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número 
# entero) 
numero=int(input('Introduce 1 número de 1 a 99'))
if(numero>=10):
    print('2 digitos')
else:
    print('1 digito')