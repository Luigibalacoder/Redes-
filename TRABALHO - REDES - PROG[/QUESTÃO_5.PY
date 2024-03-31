# Programa para administração de estacionamento 


minutosper = int(input("informe quantos minutos o condutor permaneceu no estacionamento : "))

h = minutosper // 60

if minutosper % 60 > 0:
    h += 1

valorTotal = 0

if h <= 2:
    valorTotal = h * 8

elif h <= 4:
    valorTotal = 16 +(h-2)*5

elif h <= 12:
    valorTotal = 26 +(h-4)*3

else:
    valorTotal = 30

print(f"o Condutor deverá pagar R$ {valorTotal:.2f}")