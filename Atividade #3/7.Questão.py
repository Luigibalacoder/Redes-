import os

dirArquivos = os.path.abspath(__file__)
dirArquivos = os.path.dirname(dirArquivos)


arqentrada= open (dirArquivos + '\\alunos_ifrn.csv','r',encoding='utf-8')
    
leiturarq = arqentrada.readlines()


campus_counts = {}
ano_counts = {}
curso_counts = {}

total_alunos = 0


for line in leiturarq:
    parts = line.strip().split(';')
    if len(parts) >= 8:
        campus = parts[7].strip()
        ano = parts[5][:4].strip()
        curso = parts[4].strip()
        
        
        if campus:
            if campus not in campus_counts:
                campus_counts[campus] = 0
            campus_counts[campus] += 1
        
        
        if ano:
            if ano not in ano_counts:
                ano_counts[ano] = 0
            ano_counts[ano] += 1
        

        if curso and campus:
            if campus not in curso_counts:
                curso_counts[campus] = {}
            if curso not in curso_counts[campus]:
                curso_counts[campus][curso] = 0
            curso_counts[campus][curso] += 1
        
        total_alunos += 1

campus_list = []
for campus, count in campus_counts.items():
    percentual = (count / total_alunos) * 100
    campus_list.append([campus, count, round(percentual, 2)])


with open('alunos_ifrn_campus.csv', 'w', encoding='utf-8') as file:
    for item in campus_list:
        file.write(f"{item[0]};;{item[1]};;{item[2]}\n")
ano_list = []
for ano, count in ano_counts.items():
    ano_list.append([ano, count])


with open('alunos_ifrn_ano.csv', 'w', encoding='utf-8') as file:
    for item in ano_list:
        file.write(f"{item[0]};;{item[1]}\n")

print("Campi disponíveis:")
for campus in campus_counts.keys():
    print(campus)
    
escolha = input("Escolha um campus: ").strip()

if escolha in curso_counts:
    curso_list = []
    for curso, count in curso_counts[escolha].items():
        curso_list.append([curso, count])

    with open('alunos_ifrn_campus_curso.csv', 'w', encoding='utf-8') as file:
        for item in curso_list:
            file.write(f"{item[0]};{item[1]}\n")
else:
    print("Campus escolhido invalido.")
