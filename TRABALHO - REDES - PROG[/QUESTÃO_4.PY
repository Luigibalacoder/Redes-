import sys


diaI = int(input("Digite o dia inicial: "))
mesI = int(input("Digite o mês inicial: "))

diaF = int(input("Digite o dia final: "))
mesF = int(input("Digite o mês final: "))

if mesI > mesF or (mesI == mesF and diaI > diaF):
    print("A data inicial não pode ser maior que data final.")
    sys.exit()

# Número de dias da data inicial
diasDataInicial = 0

if mesI > 1:
    diasDataInicial += 31  

if mesI > 2:
    diasDataInicial += 28  

if mesI > 3:
    diasDataInicial += 31  

if mesI > 4:
    diasDataInicial += 30  

if mesI > 5:
    diasDataInicial += 31  

if mesI > 6:
    diasDataInicial += 30  

if mesI > 7:
    diasDataInicial += 31  

if mesI > 8:
    diasDataInicial += 31  

if mesI > 9:
    diasDataInicial += 30  

if mesI > 10:
    diasDataInicial += 31  

if mesI > 11:
    diasDataInicial += 30  

diasDataInicial += diaI

# Número de dias da data final
diasDataFinal = 0
if mesF > 1:
    diasDataFinal += 31  

if mesF > 2:
    diasDataFinal += 28  

if mesF > 3:
    diasDataFinal += 31  

if mesF > 4:
    diasDataFinal += 30  

if mesF > 5:
    diasDataFinal += 31  

if mesF > 6:
    diasDataFinal += 30  

if mesF > 7:
    diasDataFinal += 31 

if mesF > 8:
    diasDataFinal += 31  

if mesF > 9:
    diasDataFinal += 30  

if mesF > 10:
    diasDataFinal += 31  

if mesF > 11:
    diasDataFinal += 30 

diasDataFinal += diaF

diferenca_dias = diasDataFinal - diasDataInicial
print(f"{diaI:02} de {mesI:02} até {diaF:02} de {mesF:02} - {diferenca_dias} dias.")