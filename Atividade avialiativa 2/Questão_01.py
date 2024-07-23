import sys 



Material = float(input('Insira a massa do material radioativo em gramas: '))


massa_final = 0.5
tempo_seg = 0 

if Material < 0.0:
    sys.exit('Insira um valor interio positvo')

else:


    print (f'Massa inicial de{Material}g')

    while Material > massa_final:
        Material /= 2
        tempo_seg += 50

    
    minutos = tempo_seg //60
    hora = minutos // 60
    segundos = tempo_seg % 60


    print (f'Massa final de{Material}g')
    print (f'tempo de decaimento:{minutos}:{segundos} ')
