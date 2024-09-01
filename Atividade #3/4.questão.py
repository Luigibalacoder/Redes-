import random,sys
n=int(input("Informe a quantidade de dimensões da lista: "))
if n<0:sys.exit('Informe uma quantidade positiva para da certo!')
list=[random.randint(0,99)for _ in range(n)]
list.sort()

soma=0
mediana=0
tamanholista=len(list)
indicmediana=tamanholista//2

if tamanholista % 2 == 0:
    mediana= (list[indicmediana-1] + list[indicmediana]) / 2         #calc mediana
else:
    mediana=list[indicmediana]

for i in list:                       #cal media
    soma+=i
media=soma/tamanholista

somaquadrado=0
for x in list:                            #calc variancia_populacional
    somaquadrado+= (x-media)**2
variancia_populacional=somaquadrado/tamanholista

desvio_padraopop= variancia_populacional ** 0.5

print(f"\nLista gerada aleatoriamente {list}\nMedia dos valores {media: }\nMediana {mediana}\nVariancia populacional {variancia_populacional: .3f}\nDesvio Padrão populacional {desvio_padraopop :.3f}")