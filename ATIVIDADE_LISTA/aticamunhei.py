import sys
import random

lst = []
tamanho_da_lista = int(input('Informe o tamanho de elementos da lista entre 7 e 60: '))
if  tamanho_da_lista >60 or tamanho_da_lista <7:
    sys.exit('Infome um número entre 7 e 60')
    

else:
    while len(lst) < tamanho_da_lista:
        a=(random.randint(0,60))
        if a not in lst:
            lst.append(a)
    nomearq = Lista    
   
        
        
    lista_arrumada = sorted(lst)
    print(f'{lst} \n {lista_arrumada}')