x=float(input('Informe as cordenadas iniciais (X) do robo: '))
y=float(input('Informe as cordenadas iniciais (Y) do robo: '))
posicao=str(input('informe em palavras como vai ser o deslocamento do robo: ').upper())
xf=0    
yf=0
mov_invalido='' 
for i in posicao:
    if i =='U':           
        yf= yf +1            
        mov_invalido+=i
    elif i =='D':          
        yf=yf -1              
        mov_invalido+=i
    elif i =='R':          
        xf=xf+1
        mov_invalido+=i
    elif i =='L':             
        xf=xf-1
        mov_invalido+=i      
    elif i =='O':            
        xf= xf-1
        yf= yf+1        
        mov_invalido+=i
    elif i =='N':          
        xf=xf+1
        yf=yf+1
        mov_invalido+=i
    elif i =='E':           
        xf= xf+1
        yf=yf-1
        mov_invalido+=i
    elif i =='W':           
        xf=xf-1
        yf=yf-1
        mov_invalido+=i
corfinalX= x+xf                 
corfinalY= y+yf                

print(f"A POSIÇÃO INICIAL \n   CORDENADA X: {x} CORDENADA Y: {y}")         
if  x >0 and y >0: print( "   O ROBÔ COMEÇOU NO 1 QUADRANTE")

elif  x <0 and y >0: print( "   O ROBÔ COMEÇOU NO 2 QUADRANTE")
elif  x <0 and y<0: print( "   O ROBÔ COMEÇOU NO 3 QUADRANTE")                              
elif  x > 0 and y < 0: print( "   O ROBÔ COMEÇOU NO 4 QUADRANTE")
elif  x == 0 and y == 0: print( "   O ROBÔ COMEÇOU NA ORIGEM")
elif  x == 0 : print( "   O ROBÔ INICIOU NO EIXO X ")

else : print( "   O ROBÔ INICIOU NO EIXO Y ")

print(f"A POSIÇÃO FINAL \n   CORDENADA X: {x+xf} CORDENADA Y: {y+yf}")  
if  corfinalX >0 and corfinalY >0: print( "   O ROBÔ TERMINOU NO 1 QUADRANTE")

elif  corfinalX <0 and corfinalY >0: print( "   O ROBÔ TERMINOU NO 2 QUADRANTE")                 
elif  corfinalX <0 and corfinalY <0: print( "   O ROBÔ TERMINOU NO 3 QUADRANTE")
elif  corfinalX > 0 and corfinalY < 0: print( "   O ROBÔ TERMINOU NO 4 QUADRANTE")
elif  corfinalX == 0 and corfinalY == 0: print( "   O ROBÔ ESTA NA ORIGEM")
elif  corfinalX == 0 : print( "   O ROBÔ ESTA NO EIXO X ")

else : print( "   O ROBÔ ESTA NO EIXO Y ")

print(f" MOVIMENTOS DO ROBÔ ")                     
print(f"   TEVE {len(mov_invalido)} MOVIMENTO EXECUTADOS AO TODO\n   ESSES FORAM OS MOVIMENTOS VALIDOS EXECUTADOS: {mov_invalido}")