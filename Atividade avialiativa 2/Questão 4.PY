
limite = 1000000


for numero in range(10, limite):
    if numero % 2 == 0 or numero % 5 == 0:
       
        soma_potencias = 0
        temp_numero = numero
        while temp_numero > 0:
            digito = temp_numero % 10
            soma_potencias += digito **5
            temp_numero //= 10
        
        
        if soma_potencias == numero:
            print(numero)