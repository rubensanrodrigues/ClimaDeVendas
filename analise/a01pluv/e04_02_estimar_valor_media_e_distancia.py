import csv
import json

def estimar_ibitinga_media_e_distancia():
    e01_dir = 'e01/'
    e04_dir = 'e04/'

    # Índices das colunas no CSV
    colunas_estacoes = {
        'A737_IBITINGA': 1,
        'A705_BAURU': 2,
        'A711_SAOCARLOS': 3,
        'A764_BEBEDOURO': 4,
        'A727_LINS': 5,
    }

    # 1. Carrega os pesos combinados (média histórica + distância)
    with open(f'{e04_dir}pesos_media_e_distancia.json', 'r') as arquivo_json:
        pesos_ponderados = json.load(arquivo_json)

    # 2. Lê os dados e aplica as estimativas
    with open(f'{e01_dir}dados_estmet_join.csv', newline='', encoding='utf-8') as csvfile, \
         open(f'{e04_dir}dados_estimado_valor_media_e_distancia.csv', 'w', newline='', encoding='utf-8') as f_saida:
        
        leitor = csv.reader(csvfile, delimiter=';')
        escritor = csv.writer(f_saida, delimiter=';')
        
        for i, linha in enumerate(leitor):
            if i == 0:
                escritor.writerow(linha)
                continue  # pula o cabeçalho

            valor_ibitinga = linha[colunas_estacoes['A737_IBITINGA']].strip()

            # Se IBITINGA estiver vazio ou com valor nulo
            if valor_ibitinga == '' or valor_ibitinga == '0.0':
                ibitinga_estimado = 0.0
                estacoes_validas = 0

                for estacao, indice in colunas_estacoes.items():
                    if estacao == 'A737_IBITINGA':
                        continue
                    try:
                        valor = float(linha[indice].strip())
                        peso = pesos_ponderados[estacao]
                        ibitinga_estimado += valor * peso
                        estacoes_validas += 1
                    except (ValueError, IndexError):
                        continue  # ignora valores ausentes ou inválidos

                # Se houver dados suficientes, aplica a estimativa
                if estacoes_validas >= 2:
                    linha[colunas_estacoes['A737_IBITINGA']] = f'{ibitinga_estimado:.2f}'
                else:
                    linha[colunas_estacoes['A737_IBITINGA']] = '0.0'

            # Escreve linha (estimada ou original)
            escritor.writerow(linha)

    print(f"Arquivo salvo: {e04_dir}dados_estimado_valor_media_e_distancia.csv")

if __name__ == "__main__":
    estimar_ibitinga_media_e_distancia()
