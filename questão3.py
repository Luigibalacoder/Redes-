
print('Bem vindo ao seu computador de bordo')



horapartida,minutopartida = (input('infome o horario quando sairam 00:00')).split(":")
horapartida, minutopartida = int(horapartida), int(minutopartida)

horachegada,minutochegada = (input('Digite a hora de Chegada 00:00 ')).split(":")
horachegada,minutochegada = int(horachegada), int(minutochegada)

descanso = int(input('informe quantos segundos ficaram parados para descansar:')) //3600

combustivel = float(input('quantos Litros de Combustível gastaram'))
preço_combustivel = float(input('Preço da Gasosa'))

distancia = float(input('Quantos Km de viagem: '))

if horachegada < horapartida:
    tempo_viagem = ((((horachegada + 12) +(minutochegada/60)) - ((horapartida - 12) + (minutopartida/60)))* 3600) + descanso
    VmG = (distancia/(tempo_viagem / 3600))
    Vmm = (distancia/(tempo_viagem /3600)) - descanso

    custo_viagem = combustivel*preço_combustivel
    desmpenhokml = distancia/combustivel
    print(f'a viagem durou {tempo_viagem} , Em uma velocidade média global {VmG} , Velocidade media em moviemnto de {Vmm} custou {custo_viagem} , com um desempenho de {desmpenhokml} ')


else: 
    tempo_viagem = ((horachegada + (minutochegada/60)) - (horapartida + (minutopartida/60)) *3600) + descanso

    VmG = (distancia/(tempo_viagem / 3600))
    Vmm = (distancia/(tempo_viagem / 3600)) - descanso

    custo_viagem = combustivel*preço_combustivel

    desmpenhokml = distancia/combustivel
    desmpenhokml = distancia/combustivel
    desempenholh = combustivel/(tempo_viagem / 3600)
    desempenhorl = distancia/preço_combustivel




    print(f'a viagem durou {tempo_viagem} , Em uma velocidade média global {VmG} , Velocidade media em moviemnto de {Vmm} custou {custo_viagem} , com um desempenho de {desmpenhokml} , {desempenholh} , {desempenhorl} ')

