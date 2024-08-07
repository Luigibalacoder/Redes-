import sys

num = int(input('Informe um número que desaja saber se ele é narcisista: '))

num_str = str(num)
contador = 0
armstrongando = 0
if num < 0:
    sys.exit('Informe um Número positivo') 

else:
    while num > 0:
        num //= 10
        contador += 1
    for i in num_str:
        armstrongando += int(i)**contador
if int(num_str) == armstrongando:
    print(f'Parabéns o numero {num_str} é um número de Armstrong')
else:
    print(f'Ah esse não é um numero de Armostrong, porém tente novamente ')

