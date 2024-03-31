import math
import sys

lado1 = float(input('Informe o lado 1 do triangulo'))
lado2 = float(input('Informe o lado 2 do triangulo'))
lado3 = float(input('Informe o lado 3 do triangulo'))

#Verificando se é um triangulo
if lado1 + lado2 <= lado3 or lado2 + lado3 <= lado1 or lado3 + lado1 <= lado2:
    print('Não é um triangulo')
    sys.exit()

print('Tipo do triângulo:') 

    #verificando pro lado
if (lado1 == lado2 == lado3):
    print('Triângulo Equilatero ')

elif (lado1 == lado2 != lado3) or (lado1 == lado3 != lado2) or (lado2 == lado3 != lado1):
    print('é um triangulo Isóceles ')
else:
    print('é um triângulo escaleno ')

print('Tipo do triângulo pelo ângulo: ')
#calculo do coseno 

radianosa = math.acos((lado2 ** 2 + lado3 ** 2 - lado1 ** 2) / (2* lado2 * lado3))
radianosb = math.acos((lado1 ** 2 + lado3 ** 2 - lado2 **2) /(2 * lado1 * lado3))
radianosc = math.acos((lado2 ** 2 + lado1 ** 2 - lado3 **2) / (2* lado1 * lado2))

grausa = math.degrees(radianosa)
grausb = math.degrees(radianosb)
grausc = math.degrees(radianosc)

#tipo do triangulo pelos graus 
if grausa < 90 and grausb < 90 and grausc < 90:
    print('É um acutângulo')

elif grausa == 90 and grausb == 90 and grausc == 90:
    print('É um Retângulo')
else:
    print('é um obtusângulo')