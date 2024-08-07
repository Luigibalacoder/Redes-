import sys
palavra=str(input('Informe uma palavra que a ser descoberta: ').upper())
dica= str(input('Ajude o jogador com uma dica : ').upper())
erro=0
nova='_' * len(palavra)                      
letradigitadas=''

while erro !=6 and  '_' in nova :                            
    print(f"Essas foram as letras digitadas: {letradigitadas}")
    print(f"PALAVRA: {nova}")
    letra=str(input('INFORME UMA LETRA: ').upper())   
    noval=''
    letradigitadas+=letra
    if  letra in palavra:
        for i in range(len(palavra)):                                 
            if palavra[i] == letra:                                          
                noval += letra                
            else:
                noval+= nova[i]
        nova=noval       
    else:                            
        erro+=1                                           
        print(f'ERROU {erro} VEZE(s),VOCE POSSUI {6 - erro} CHANCES.\nO TEMA DA PALAVRA E {dica}, E A PALAVRA POSSUI {len(palavra)} LETRAS')

    print()
if erro == 6:                                  
    sys.exit('VOCÊ PERDEU,POIS ERROU 6 VEZES  DIGITANDO A PALAVRA ERRADA')      
elif erro < 6:
    print(f" PARABENS,VOCÊ DESCOBRIU A PALAVRA QUE E {nova} !!")