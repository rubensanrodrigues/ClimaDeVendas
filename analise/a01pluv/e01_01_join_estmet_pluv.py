import csv

def juntar_dados_meteorologicos():
    # Lista dos arquivos a serem lidos
    arquivos = [
        'dados_A737_IBITINGA.csv',
        'dados_A705_BAURU.csv',
        'dados_A711_SAO-CARLOS.csv',
        'dados_A764_BEBEDOURO.csv',
        'dados_A727_LINS.csv'
    ]

    # Diretórios fixos
    dados_dir = 'dados/'
    e01_dir = 'e01/'

    # Lista para guardar os dados de cada arquivo como {data: valor}
    dados_por_arquivo = []

    # Conjunto com todas as datas únicas encontradas nos arquivos
    todas_as_datas = set()

    # 1. Ler os dados de cada arquivo e armazenar em dicionários
    for nome_arquivo in arquivos:
        dados = {}
        caminho = f'{dados_dir}{nome_arquivo}'
        with open(caminho, newline='', encoding='utf-8') as f:
            leitor = csv.reader(f, delimiter=';')
            for i, linha in enumerate(leitor):
                # Pula as primeiras 11 linhas (cabeçalho e metadados)
                if i < 11:
                    continue
                # Ignora linhas vazias
                if not linha:
                    continue
                # Extrai a data e o valor
                data = linha[0]
                try:
                    valor = float(linha[1].replace(',', '.'))
                    dados[data] = valor
                    todas_as_datas.add(data)
                except ValueError:
                    # Ignora valores inválidos (ex: texto no lugar de número)
                    continue
        dados_por_arquivo.append(dados)

    # 2. Criar arquivo de saída com os dados combinados
    caminho_saida = f'{e01_dir}dados_estmet_join.csv'
    with open(caminho_saida, 'w', newline='', encoding='utf-8') as f_saida:
        escritor = csv.writer(f_saida, delimiter=';')

        # Cabeçalho: data, nomeArquivo1, nomeArquivo2, ...
        cabecalho = ['data'] + arquivos
        escritor.writerow(cabecalho)

        # 3. Escrever os dados linha por linha
        for data in sorted(todas_as_datas):
            linha = [data]
            for i, dados in enumerate(dados_por_arquivo):
                if i == 0:
                    valor = dados.get(data, '')  # Primeiro arquivo deixa vazio se não houver dado
                else:
                    valor = dados.get(data, '0.0')  # Demais arquivos usam 0.0 como padrão
                linha.append(valor)
            escritor.writerow(linha)

    print(f"Arquivo '{caminho_saida}' criado com sucesso.")

# Executa a função se este script for chamado diretamente
if __name__ == "__main__":
    juntar_dados_meteorologicos()
