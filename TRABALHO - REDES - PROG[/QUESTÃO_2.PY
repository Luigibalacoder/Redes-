import sys


saque = float(input('informe o quanto deseja sacar'))

if saque > 0:
    cedula200 = (saque // 200)  
    cedula100 = (saque - (cedula200*200)) // 100 
    cedula50 = (saque - ((saque // 100)*100)) // 50
    cedula20 = ((saque - ((saque // 100)*100)) % 50) // 20 
    cedula10 = (((saque - ((saque // 100)*100)) % 50) % 20) // 10
    cedula5 = (((saque - ((saque // 100)*100)) % 50) % 10) // 5
    cedula2 = (((saque - ((saque // 100)*100)) % 50) % 5) // 2
    moeda1 = (((saque - ((saque // 100)*100)) % 5)) % 2
    moeda050 = (saque - (saque // 1)) // 0.5
    moeda025 = (saque % 0.5 ) // 0.25
    moeda010 = (saque % 0.25) // 0.10
    moeda005 = (saque % 0.10) // 0.05
     

print(f'{cedula200:.0f} cedulas de 200 ')
print(f'{cedula100:.0f} cedulas de 100 ')
print(f'{cedula50:.0f} cedulas de 50 ')
print(f'{cedula20:.0f} cedulas de 20 ')
print(f'{cedula10:.0f} cedulas de 10 ')
print(f'{cedula5:.0f} cedulas de 5 ')
print(f'{cedula2:.0f} cedulas de 2 ')
print(f'{moeda1:.0f} moedas de 1 ')
print(f'{moeda050:.0f} moedas de 0,25 centavos')
print(f'{moeda010} moedas de 0,10 centavos')
print(f'{moeda005} moedas de 0,05 centavos')




