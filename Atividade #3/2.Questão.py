x=int(input("Informe a Quantidade de elementos na lista: "))
list=[]

while True:
    n=int(input("informe um valor: "))
    if n==0: break
    elif len(list) == x:
        del list[-1]
        list.append(n)
        list.sort()
        print(list)
    else:
        list.append(n)
        list.sort()
        print(list)
    
    