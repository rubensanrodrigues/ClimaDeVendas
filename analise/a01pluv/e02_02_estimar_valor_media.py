import csv
import json

def estimar_valores_ibitinga():
    # Diretórios de entrada e saída
    e01_dir = 'e01/'
    e02_dir = 'e02/'

    # Mapeia as estações aos índices das colunas no CSV
    colunas_estacoes = {
        'A737_IBITINGA': 1,
        'A705_BAURU': 2,
        'A711_SAOCARLOS': 3,
        'A764_BEBEDOURO': 4,
        'A727_LINS': 5,
    }

    # 1. Carrega os pesos do arquivo JSON
    caminho_pesos = f'{e02_dir}pesos.json'
    with open(caminho_pesos, 'r') as arquivo_json:
        pesos = json.load(arquivo_json)

    # 2. Abre os arquivos de entrada e saída
    caminho_csv = f'{e01_dir}dados_estmet_join.csv'
    caminho_saida = f'{e02_dir}dados_estimado_valor_media.csv'
    
    with open(caminho_csv, newline='', encoding='utf-8') as csvfile, \
         open(caminho_saida, 'w', newline='', encoding='utf-8') as f_saida:

        leitor = csv.reader(csvfile, delimiter=';')
        escritor = csv.writer(f_saida, delimiter=';')

        for i, linha in enumerate(leitor):
            # Cabeçalho: apenas copia
            if i == 0:
                escritor.writerow(linha)
                continue

            # Valor atual de IBITINGA
            ibitinga_valor = linha[colunas_estacoes['A737_IBITINGA']].strip()

            # Se estiver vazio, tenta estimar
            if ibitinga_valor == '':
                soma_presentes = 0.0
                peso_ibitinga = pesos['A737_IBITINGA']

                # Soma os valores das outras estações disponíveis
                for estacao, indice in colunas_estacoes.items():
                    if estacao == 'A737_IBITINGA':
                        continue
                    try:
                        valor = float(linha[indice].strip())
                        soma_presentes += valor
                    except (ValueError, IndexError):
                        continue  # ignora valores ausentes ou inválidos

                # Estima valor para IBITINGA usando os pesos
                if soma_presentes > 0 and peso_ibitinga < 1.0:
                    ibitinga_estimada = soma_presentes * peso_ibitinga / (1 - peso_ibitinga)
                    linha[colunas_estacoes['A737_IBITINGA']] = f'{ibitinga_estimada:.1f}'
                else:
                    linha[colunas_estacoes['A737_IBITINGA']] = '0.0'

            # Escreve linha modificada no arquivo de saída
            escritor.writerow(linha)

    print(f"Arquivo com valores estimados salvo em: {caminho_saida}")

# Executa a função se o script for chamado diretamente
if __name__ == "__main__":
    estimar_valores_ibitinga()
