import sys
palavra=str(input('Informe uma palavra que a ser descoberta: ').upper())
dica= str(input('Informe o tema da palavra para ajudar o jogador: ').upper())
erro=0
nova='_' * len(palavra)                      #para imprimir a str '-' do tamanho da palavra
letradigitadas=''

while erro !=6 and  '_' in nova :                            #while funciona ate erro e nova não serem iguais ao especificado
    print(f"Essas foram as letras digitadas: {letradigitadas}")
    print(f"PALAVRA: {nova}")
    letra=str(input('INFORME UMA LETRA: ').upper())   
    noval=''
    letradigitadas+=letra
    if  letra in palavra:
        for i in range(len(palavra)):                                 
            if palavra[i] == letra:                                          #objetivo de checar letra por letra individualmente
                noval += letra                
            else:
                noval+= nova[i]
        nova=noval       
    else:                            
        erro+=1                                           #Aonde contabiliza os erros e informa algumas dicas para ajudar o jogador
        print(f'ERROU {erro} VEZE(s),VOCE POSSUI {6 - erro} CHANCES.\nO TEMA DA PALAVRA E {dica}, E A PALAVRA POSSUI {len(palavra)} LETRAS')

    print()
if erro == 6:                                  #mensagem apenas para mostrar ao usuario se perdeu ou venceu
    sys.exit('VOCÊ PERDEU,POIS ERROU 6 VEZES  DIGITANDO A PALAVRA ERRADA')      
elif erro < 6:
    print(f"{'-'*15} PARABENS,VOCÊ DESCOBRIU A PALAVRA QUE E {nova} !!{'-'*15}")