import sys


num = int(input('insira um número inteiro positivo: '))

if num <0:
    sys.exit('Informe um número positivo')
else:
    contador = 0 

    while num > 0:
        num //= 10
        contador += 1 
    
    print(f'O valor informado tem {contador} Dígitos')
    