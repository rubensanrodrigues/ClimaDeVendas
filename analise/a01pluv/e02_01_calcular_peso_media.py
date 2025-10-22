import csv
import json

def calcular_pesos_estacoes():
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

    # Inicializa dicionário para somar os valores de cada estação
    somas = {nome: 0.0 for nome in colunas_estacoes}

    # 1. Leitura do CSV e cálculo das somas
    caminho_entrada = f'{e01_dir}dados_estmet_join.csv'
    with open(caminho_entrada, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile, delimiter=';')
        for i, linha in enumerate(leitor):
            if i == 0:
                continue  # pula o cabeçalho

            # Remove espaços em branco das colunas relevantes
            campos = [linha[j].strip() for j in range(1, 6)]

            # Garante que todas as colunas possuem valor
            if all(campos):
                # Ignora linhas onde IBITINGA está com valor "0.0"
                if linha[colunas_estacoes['A737_IBITINGA']] == '0.0':
                    continue

                # Soma os valores válidos
                for estacao, indice in colunas_estacoes.items():
                    try:
                        valor = float(linha[indice].strip())
                        somas[estacao] += valor
                    except ValueError:
                        print(f"[VALOR INVÁLIDO] Linha {i}, estação {estacao}: '{linha[indice]}'")

    # 2. Calcula o total acumulado
    total = sum(somas.values())
    if total == 0:
        print("Não foi possível calcular os pesos: total acumulado é zero.")
        return

    # 3. Calcula os pesos relativos de cada estação
    pesos = {}
    for estacao, valor in somas.items():
        peso = valor / total
        pesos[estacao] = peso

    # 4. Salva os pesos em um arquivo JSON
    caminho_saida = f'{e02_dir}pesos.json'
    with open(caminho_saida, 'w') as arquivo_json:
        json.dump(pesos, arquivo_json, indent=4)

    print(f"Pesos calculados com sucesso e salvos em: {caminho_saida}")

# Executa a função se o script for chamado diretamente
if __name__ == "__main__":
    calcular_pesos_estacoes()
