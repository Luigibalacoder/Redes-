# Olá, programa feito para você calcular a soma dos algorismo de um numero


import operator
import sys

n = int(input('digite um numero de até 4 digitos'))

varmil = (n // 1000 ) 

varcent = ((n - ((varmil * 1000))) // 100) 

vardez = ((n - ((varmil * 1000))) - (varcent * 100)) // 10 

varuni = (n - ((n // 10 ) *10))



if 0 <= n <= 9999:
    soma = varmil + varcent + vardez + varuni 

    print(soma)
else:
    print('Numero Inválido precisa ser maior do que 0 ')
    SystemExit()