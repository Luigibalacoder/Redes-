import sys


x = int(input('Adicione números a lista'))
    
lst=[x]

while x != 0 :
    x = int(input('Adicione números a lista'))
    lst.append(x)

soma = sum(lst)
media = soma/len(lst)
lst.sort()

print(f'Os números adicionados à lista foram {lst} e a soma dos respectivos é {soma} e a Média é {media}')