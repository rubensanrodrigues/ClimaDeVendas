import csv
import json

def estimar_valores_ibitinga_por_distancia():
    # Diretórios fixos
    e01_dir = 'e01/'
    e03_dir = 'e03/'

    # Mapeia as estações às colunas do CSV
    colunas_estacoes = {
        'A737_IBITINGA': 1,
        'A705_BAURU': 2,
        'A711_SAOCARLOS': 3,
        'A764_BEBEDOURO': 4,
        'A727_LINS': 5,
    }

    # 1. Lê os pesos baseados em distância
    caminho_pesos = f'{e03_dir}pesos_distancia.json'
    with open(caminho_pesos, 'r') as arquivo_json:
        pesos = json.load(arquivo_json)

    # 2. Processa o CSV original e estima valores de IBITINGA quando necessário
    caminho_csv_entrada = f'{e01_dir}dados_estmet_join.csv'
    caminho_csv_saida = f'{e03_dir}dados_estimado_valor_distancia.csv'

    with open(caminho_csv_entrada, newline='', encoding='utf-8') as csvfile, \
         open(caminho_csv_saida, 'w', newline='', encoding='utf-8') as f_saida:

        leitor = csv.reader(csvfile, delimiter=';')
        escritor = csv.writer(f_saida, delimiter=';')

        for i, linha in enumerate(leitor):
            # Cabeçalho: apenas copia
            if i == 0:
                escritor.writerow(linha)
                continue

            # Valor atual de IBITINGA
            ibitinga_valor = linha[colunas_estacoes['A737_IBITINGA']].strip()

            # Se estiver ausente, estimamos
            if ibitinga_valor == '':
                eventos = {}

                # Coleta os valores válidos das outras estações
                for estacao, indice in colunas_estacoes.items():
                    if estacao == 'A737_IBITINGA':
                        continue
                    try:
                        valor = float(linha[indice].strip())
                        eventos[estacao] = valor
                    except (ValueError, IndexError):
                        continue  # Ignora valores ausentes ou inválidos

                # Estima IBITINGA com base nos pesos por distância
                ibitinga_estimada = sum(
                    pesos[estacao] * eventos[estacao]
                    for estacao in eventos
                )

                if ibitinga_estimada > 0:
                    linha[colunas_estacoes['A737_IBITINGA']] = f'{ibitinga_estimada:.1f}'
                else:
                    linha[colunas_estacoes['A737_IBITINGA']] = '0.0'

            # Escreve a linha ajustada no novo arquivo
            escritor.writerow(linha)

    print(f"Arquivo gerado com estimativas por distância: {caminho_csv_saida}")

# Executa a função se o script for chamado diretamente
if __name__ == "__main__":
    estimar_valores_ibitinga_por_distancia()
