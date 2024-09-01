import random,sys
n=int(input("Informe o tamanho da lista deve ser entre 7 e 60: "))
if  n< 7 or n> 60:sys.exit("Informe um tamanho entre 7 e 60")
lista=[]
contador=1
while contador <= n:
    valor=random.randint(1,60)
    if valor not in lista:
        lista.append(valor)
        contador+=1
print(lista)
combinacoes = []
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        for k in range(j + 1, len(lista)):
            for l in range(k + 1, len(lista)):
                for m in range(l + 1, len(lista)):
                    for o in range(m + 1, len(lista)):
                        combinacoes.append([lista[i], lista[j], lista[k], lista[l], lista[m], lista[o]])


f = open('numeros_escolhidos.txt', 'w')
f.write(';'.join(map(str, lista)))
f.close()

f = open('combinacoes.txt', 'w')
for x in combinacoes:
    f.write(';'.join(map(str, x)) + '\n')
f.close()

combinacoestotal = len(combinacoes)

print(f"Total de combinações: {combinacoestotal}")
