valor1, valor2 = int(input('Insira o primeiro valor: ')), int(input('Insira o Segundo valor: '))

var = 0

while ((valor1 % valor2) >0):
    var = valor1 % valor2
    valor1 = valor2 
    valor2 = var 


