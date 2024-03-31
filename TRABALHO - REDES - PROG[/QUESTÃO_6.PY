from datetime import *
import sys

sexo = str(input("Digite seu sexo (masculino/feminino): "))

dataNascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
inicioCont = input("Data de início da contribuição (DD/MM/AAAA): ")

dataNascimento = datetime.strptime(dataNascimento, "%d/%m/%Y").date()
inicioCont = datetime.strptime(inicioCont, "%d/%m/%Y").date()

idade = (datetime.today().date() - dataNascimento).days // 365
tempodecont = (datetime.today().date() - inicioCont).days // 365

#Aposentadoria por idade 


if idade >= 65  and sexo == 'masculino' and tempodecont >= 15:
    print('Parabéns pode se aposentar, obrigado pelos seus serviços.')
    sys.exit()

elif idade >= 62 and sexo == 'feminino' and tempodecont >= 15:
    print('Parabéns você já pode se aposentar, obrigado pelos seus serviços.')
    sys.exit()



# Aposentadoria por tempo de contribuição

if sexo == 'masculino' and tempodecont >= 35:
    print('pode se aposentar, pelo seu tempo de contribuição.')
    sys.exit()

elif sexo == 'feminino' and tempodecont >= 30:
    print('pode se aposentar, pelo seu tempo de contribuição.')
    sys.exit()

else: 
    print('não pode se aposentar.')
    sys.exit()




