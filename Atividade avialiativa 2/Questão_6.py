import sys
valor_ini=int(input('Informe um valor inteiro inicial da PG: '))
razao=float(input('Informe a Razao da PG: '))
vqntd=int(input('Informe a quantidade de elementos positivo de uma  PG: '))
valorpg=valor_ini
soma=valor_ini

       
for i in range (2,vqntd+1):
    print(f'o valor da PG({i})={valorpg} * {razao} = {valorpg*razao}')                
    valorpg*=razao  
    soma+=valorpg

print(f'A soma dos valores dessa PG são: {soma}')



if vqntd<0:           
    sys.exit('Quantidade de elementos da PG tem que ser positivos ')

elif razao == 1 or razao == 0:
    print("A PG e  uma constante")                 
elif razao < 0 :
    print("A PG e uma Oscilante")
elif valorpg >= 1 < razao or 0<razao<1>valorpg<0:
    print("A PG e uma crescente")
elif 0<razao<1:
    print("A PG e  uma decrescente") 

nove=int(input('informe um  valor inteiro que corresponde para saber ele em sua enezima posição: '))
if nove < 0:                      
    sys.exit('Informe uma quantidade de elementos positivos da PG')    
termoene= valor_ini *(razao**(nove-1))      
print(f'o valor da enezima posição  {nove} Da pg acima e {termoene:,}')