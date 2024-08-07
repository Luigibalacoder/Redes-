import sys


num=int(input("Informe numero inteiro e positivo para verificar se ele é triangular: "))

contador=1
numero_tri=0

if num<0:
    sys.exit("Informe um numero positivo para da certo o cálculo")

while  True:
    numero_tri=(contador/2) * (2*1+(contador-1)*1)                
    contador+=1                                                    
    if numero_tri == num:                                       
        sys.exit(f'{num} É um numero triangula') 
    if numero_tri> num:                                  
        sys.exit(f'{num} Não é um numero triangular')  