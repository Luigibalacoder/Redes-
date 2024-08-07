import sys

valor_ini, razao= int(input('Informe o valor inicial da P.A')), int(input('Informe a razão da P.A'))
vqntd = int(input('Informe a quantidade de termos da P.A'))

y= valor_ini
soma = 0

for i in range (1,vqntd+1):

    valor_ini += razao
    print(f'O valor da PG{i} é {y} + {razao} = {valor_ini}')
    y = valor_ini
    soma +=valor_ini

print(f'a soma dos termos desta P.A é {soma}')

if vqntd<0:         
    sys.exit('Informe quantidade de elementos positivos da PG')
elif razao == 0:
    print("A PA e  uma constante")
elif razao>0:                                                                
    print("A PA e uma crescente")
elif razao<0: 
    print("A PA e  uma decrescente")


num=int(input('informe um outro valor inteiro que corresponde  a enezima posição dessa PA: '))

termoene= valor_ini +(num-1)*razao
print(f"o valor da enezima posição  {num} e {termoene:,}")
