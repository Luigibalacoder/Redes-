import requests, sys, datetime, json, os

def obter_moedas():
    try:
        url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=100&$format=json'
        response = requests.get(url).json()
        return [(moeda['simbolo'], moeda['nomeFormatado']) for moeda in response['value']], datetime.date.today().year
    except (requests.exceptions.RequestException, KeyError) as e:
        sys.exit(f"Erro ao obter moedas: {e}")

def obter_cotacoes(moeda, ano):
    try:
        url = (f'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
               f'@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda=%27{moeda}%27&@dataInicial=%2701-01-{ano}%27&'
               f'@dataFinalCotacao=%2712-31-{ano}%27&$format=json')
        return requests.get(url).json()
    except (requests.exceptions.RequestException, KeyError) as e:
        sys.exit(f"Erro ao obter cotações: {e}")

def calcular_medias(cotacoes):
    medias = {}
    for cotacao in cotacoes['value']:
        data = cotacao['dataHoraCotacao'].split('T')[0]
        mes = data[5:7]
        if mes not in medias:
            medias[mes] = {'mediaCompra': [], 'mediaVenda': []}
        if cotacao['cotacaoCompra'] and cotacao['cotacaoVenda']:
            medias[mes]['mediaCompra'].append(cotacao['cotacaoCompra'])
            medias[mes]['mediaVenda'].append(cotacao['cotacaoVenda'])
    
    return {mes: {'mediaCompra': round(sum(m['mediaCompra']) / len(m['mediaCompra']), 5),
                  'mediaVenda': round(sum(m['mediaVenda']) / len(m['mediaVenda']), 5)}
            for mes, m in medias.items() if m['mediaCompra'] and m['mediaVenda']}

def salvar_arquivos(medias_calculadas, moeda, ano):
    json_file = f'medias_cotacoes_{moeda}_{ano}.json'
    csv_file = f'medias_cotacoes_{moeda}_{ano}.csv'
    
    try:
        with open(json_file, 'w') as jf:
            json.dump(medias_calculadas, jf, indent=4)
        with open(csv_file, 'w') as cf:
            cf.write('moeda;mes;mediaCompra;mediaVenda\n')
            for mes, medias in medias_calculadas.items():
                cf.write(f'{moeda};{mes};{medias["mediaCompra"]};{medias["mediaVenda"]}\n')
        print("\nArquivos salvos com sucesso.")
    except IOError as e:
        sys.exit(f"Erro ao salvar arquivos: {e}")

def main():
    moedas, anoatual = obter_moedas()
    abrevmoedas, nomemoeda = zip(*moedas)  # main as listas de siglas e nomes
    
    while True:
        print("\n--- Moedas disponíveis ---")
        for sigla, nome in moedas:
            print(f'{sigla} - {nome}')
        
        moeda = input("\nInforme a sigla da moeda (ou 0 para sair): ").upper()
        if moeda == '0': break
        if moeda not in abrevmoedas:
            print("Moeda inválida. Tente novamente.")
            continue
        
        try:
            ano = int(input(f"Informe o ano (1990 a {anoatual}): "))
            if not (1990 <= ano <= anoatual):
                print("Ano inválido. Tente novamente.")
                continue
        except ValueError:
            print("Valor inválido para o ano. Tente novamente.")
            continue

        cotacoes = obter_cotacoes(moeda, ano)
        if not cotacoes.get('value'):
            print("Nenhuma cotação encontrada para o ano informado.")
            continue
        
        medias_calculadas = calcular_medias(cotacoes)
        salvar_arquivos(medias_calculadas, moeda, ano)

if __name__ == "__main__":
    main()

