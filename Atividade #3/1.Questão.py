import random

n1=int(input("Digite a quantidade de listas na matriz: "))
n2=int(input("Digite a quantidade de elementos em cada lista: "))

matriz = [[random.randint(1,100) for _ in range(n2)] for _ in range(n1)]

print(f"\nMatriz Original: \n{matriz}")

matriztransposta=[[matriz[a][b] for a in range(n1)] for b in range (n2)]

print(f"\nMatriz transposta: \n{matriztransposta}")