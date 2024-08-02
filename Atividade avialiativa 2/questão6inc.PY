valor_inicial, razao = int(input('Informe o número inicial da pg: ')), float(input('Agora sua razão: '))
valor_final = int(input('Infome até onde ela vai: '))
 
resultado = 0
print(valor_inicial)
for i in range (valor_inicial, valor_final+1):
    resultado = valor_inicial * razao
    valor_inicial = resultado

    print(resultado)
    

if razao < 0:
    print('A P.G é oscilante')
elif razao < 1 and razao > 0:
    print('A razão é decrescente e constante')
elif razao >1:
    print('Pg é crescente e consante' )

