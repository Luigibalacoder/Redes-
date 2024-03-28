from datetime import *
from dateutil import *

# Aposentadoria

Sexo = str(input('informe o sexo Masculino/Feminino: '))

Data_nasc = input('informe sua data de nascmento (DD/MM/AAAA): ')
Data_cont = input('Data de início da contribuição previdenciária (DD/MM/AAAA):')


Data_nasc = datetime.strptime(Data_nasc, '%d/%m/%y').date()
Data_cont = datetime.strptime(Data_cont, '%d/%m/%y').date()

idade = (datetime.today().date() - Data_nasc).days //365
tempo_cont = (datetime.today().date() - Data_cont).days // 365

