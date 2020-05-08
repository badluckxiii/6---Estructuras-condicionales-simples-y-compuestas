#  Realizar un programa que solicite la carga por teclado de dos números, si el
#  primero es mayor al segundo informar su suma y diferencia, 
# en caso contrario informar el producto y la división del primero respecto al
#  segundo. 
a=int(input('Valor de a:'))
b=int(input('Valor de b:'))
if a>b:
    print('La suma es',a+b,'\nLa resta es',a-b)
else:
    print('La mutiplicacion es ',b*a,'\nLa division es ',b/a)