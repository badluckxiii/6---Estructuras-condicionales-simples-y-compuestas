#  Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete
#  mostrar un mensaje "Promocionado". 
a=int(input('Nota 1:'))
b=int(input('Nota 2:'))
c=int(input('Nota 3:'))
suma=a+b+c
promedio=suma/3
if(promedio>=7):
    print('Promocionado')
else:
    print('No promocionado')