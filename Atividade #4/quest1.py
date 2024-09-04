import requests
import datetime
import json
import sys


ano_atual = datetime.date.today().year

#inputs 
moeda = input('informe o moeda ').upper()
ano_inf = int(input(f'Informe o ano que deseja para cotação da moeda - {moeda} -: '))

    
    
strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata'
strURL += '/Moedas?$top=100&$format=json'
dictMoedas = requests.get(strURL).json()
strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
strURL += f'@moeda=%27USD%27&@dataInicial=%2701-01-{ano_inf}%27&'
strURL += f'@dataFinalCotacao=%2712-31-{ano_inf}%27&$format=json'
dictCotacoes = requests.get(strURL).json()

nomemoeda  = [moeda['nomeFormatado']for moeda in dictMoedas['value']]
sigla_moeda  = [moeda['simbolo']for moeda in dictMoedas['value']]

    
#Vallida o ano:
if ano_inf > ano_atual:
    sys.exit('-ERRO- Ano informado não pode ser maior do que o ano atual ')
    
#Valida a moeda 
if moeda not in sigla_moeda:
    sys.exit('Moeda informada não existe')

dcitgeral = {nomemoeda:sigla_moeda}

print(dcitgeral)
