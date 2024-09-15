import requests
import json
from datetime import datetime
from tabulate import tabulate

# Função para solicitar o ano e validar
def solicitar_ano():
    ano_atual = datetime.now().year
    try:
        ano_informado = int(input(f"Informe o ano (2021 a {ano_atual}): "))
    except ValueError:
        print("Erro: O ano informado deve ser um número inteiro.")
        exit()

    while ano_informado < 2021 or ano_informado > ano_atual:
        try:
            ano_informado = int(input(f"Ano inválido. Informe um ano entre 2021 e {ano_atual}: "))
        except ValueError:
            print("Erro: O ano informado deve ser um número inteiro.")
            exit()

    return ano_informado

# Função para carregar os dados de acordo com o ano informado
def carregar_dados_cartola(ano_informado):
    ano_atual = datetime.now().year
    try:
        if ano_informado == ano_atual:
            strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
            dictCartola = requests.get(strURL).json()
        else:
            nome_arquivo = f'cartola_fc_{ano_informado}.json'
            with open(nome_arquivo, 'r', encoding='utf-8') as file:
                dictCartola = json.load(file)
        return dictCartola
    except requests.exceptions.RequestException as e:
        print("Erro ao fazer a requisição:", e)
        exit()
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
        exit()

# Função para exibir os esquemas táticos disponíveis
def exibir_esquemas_taticos():
    escalacao_disponiveis = {
        1: '3-4-3',
        2: '3-5-2',
        3: '4-3-3',
        4: '4-4-2',
        5: '4-5-1',
        6: '5-3-2',
        7: '5-4-1'
    }

    print("Escolha uma das escalações que estão disponíveis :")
    tabela_escalacoes = [[num, escalacao] for num, escalacao in escalacao_disponiveis.items()]
    print(tabulate(tabela_escalacoes, headers=['Número', 'Escalação'], tablefmt='grid'))

    return escalacao_disponiveis

# Função para solicitar o esquema tático desejado
def solicitar_esquema(escalacao_disponiveis):
    try:
        escalacao_escolhida = int(input("Informe o número (1 a 7) da escalação que você deseja escolher: "))
    except ValueError:
        print("Erro: A escolha deve ser um número inteiro.")
        exit()

    while escalacao_escolhida < 1 or escalacao_escolhida > 7:
        try:
            escalacao_escolhida = int(input("Escalação inválida. Escolha uma escalação dentre as apresentadas: "))
        except ValueError:
            print("Erro: A escolha deve ser um número inteiro.")
            exit()

    return escalacao_escolhida

# Função para selecionar os jogadores com as maiores pontuações
def selecionar_jogadores(dictCartola, esquema_selecionado):
    esquemas_taticos = {
        '3-4-3': {'goleiro': 1, 'zagueiro': 3, 'lateral': 0, 'meia': 4, 'atacante': 3, 'tecnico': 1},
        '3-5-2': {'goleiro': 1, 'zagueiro': 3, 'lateral': 0, 'meia': 5, 'atacante': 2, 'tecnico': 1},
        '4-3-3': {'goleiro': 1, 'zagueiro': 2, 'lateral': 2, 'meia': 3, 'atacante': 3, 'tecnico': 1},
        '4-4-2': {'goleiro': 1, 'zagueiro': 2, 'lateral': 2, 'meia': 4, 'atacante': 2, 'tecnico': 1},
        '4-5-1': {'goleiro': 1, 'zagueiro': 2, 'lateral': 2, 'meia': 5, 'atacante': 1, 'tecnico': 1},
        '5-3-2': {'goleiro': 1, 'zagueiro': 3, 'lateral': 2, 'meia': 3, 'atacante': 2, 'tecnico': 1},
        '5-4-1': {'goleiro': 1, 'zagueiro': 3, 'lateral': 2, 'meia': 4, 'atacante': 1, 'tecnico': 1},
    }

    quantidade_posicoes = esquemas_taticos[esquema_selecionado]
    selecionados = {}

    for posicao, quantidade in quantidade_posicoes.items():
        posicao_id = {
            'goleiro': 1,
            'zagueiro': 3,
            'lateral': 2,
            'meia': 4,
            'atacante': 5,
            'tecnico': 6
        }[posicao]

        jogadores = [atleta for atleta in dictCartola['atletas'] if atleta['posicao_id'] == posicao_id]

        for atleta in jogadores:
            atleta['pontuacao_total'] = round(atleta.get('media_num', 0) * atleta.get('jogos_num', 0), 2)

        jogadores = sorted(jogadores, key=lambda x: x.get('pontuacao_total', 0), reverse=True)[:quantidade]
        selecionados[posicao] = jogadores

    return selecionados

# Função para exibir a seleção final
def exibir_selecao_final(selecionados, dictCartola):
    print("\nSeleção do Cartola FC:")
    tabela_selecao = []
    for posicao in ['goleiro', 'zagueiro', 'lateral', 'meia', 'atacante', 'tecnico']:
        if posicao in selecionados:
            for atleta in selecionados[posicao]:
                clube_id = str(atleta['clube_id'])
                clube_nome = dictCartola['clubes'].get(clube_id, {}).get('nome', 'Clube Desconhecido')
                tabela_selecao.append([
                    atleta['nome'],
                    atleta['apelido'],
                    clube_nome,
                    posicao.capitalize(),
                    f"{atleta.get('pontuacao_total', 0):.2f}"
                ])
    print(tabulate(tabela_selecao, headers=['Nome', 'Apelido', 'Clube', 'Posição', 'Pontuação'], tablefmt='grid'))

# Função principal
def main():
    ano_informado = solicitar_ano()
    dictCartola = carregar_dados_cartola(ano_informado)
    escalacao_disponiveis = exibir_esquemas_taticos()
    escalacao_escolhida = solicitar_esquema(escalacao_disponiveis)
    esquema_selecionado = escalacao_disponiveis[escalacao_escolhida]
    selecionados = selecionar_jogadores(dictCartola, esquema_selecionado)
    exibir_selecao_final(selecionados, dictCartola)

# Executa o programa
if __name__ == "__main__":
    main()
