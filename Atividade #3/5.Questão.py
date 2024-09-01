gabarito = ['A', 'C', 'B', 'A', 'E', 'D', 'D', 'C', 'A', 'A']
listaalunos = [
    ['Aluno 01', 'B', 'D', 'E', 'E', 'C', 'D', 'A', 'B', 'C', 'D'],
    ['Aluno 02', 'C', 'D', 'A', 'B', 'D', 'A', 'A', 'C', 'B', 'E'],
    ['Aluno 03', 'A', 'A', 'B', 'D', 'C', 'E', 'E', 'A', 'A', 'C'],
    ['Aluno 04', 'B', 'B', 'C', 'C', 'D', 'E', 'D', 'D', 'E', 'E'],
    ['Aluno 05', 'B', 'B', 'D', 'A', 'A', 'E', 'B', 'D', 'E', 'C'],
    ['Aluno 06', 'C', 'C', 'D', 'E', 'B', 'B', 'C', 'D', 'E', 'A'],
    ['Aluno 07', 'B', 'A', 'A', 'B', 'B', 'C', 'D', 'E', 'A', 'B'],
    ['Aluno 08', 'D', 'E', 'A', 'B', 'B', 'C', 'C', 'D', 'A', 'A'],
    ['Aluno 09', 'A', 'A', 'A', 'C', 'B', 'D', 'D', 'E', 'D', 'C'],
    ['Aluno 10', 'B', 'B', 'D', 'E', 'C', 'D', 'C', 'E', 'B', 'A']
]

for x in listaalunos:
    acertos = 0
    for i in range(len(gabarito)):
        if x[i + 1] == gabarito[i]:
            acertos += 1
    x.append(acertos)

for i in range(len(listaalunos)):
    for j in range(i + 1, len(listaalunos)):
        if listaalunos[i][-1] < listaalunos[j][-1]:
            comp = listaalunos[i]
            listaalunos[i] = listaalunos[j]
            listaalunos[j] = comp


print("Este e o gabarito da prova:", gabarito)
print("\nResultados dos Alunos:")
for i in listaalunos:
    nome = i[0]
    respostas = i[1:-1]
    acertos = i[-1]
    print(f"{nome}: Respostas: {respostas}  Nota do aluno: {acertos}")