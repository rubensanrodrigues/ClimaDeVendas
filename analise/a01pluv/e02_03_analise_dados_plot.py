import pandas as pd
import matplotlib.pyplot as plt

def gerar_grafico_estimado_ibitinga():
    # Diretório de entrada e saída
    e02_dir = 'e02/'

    # 1. Lê o arquivo CSV com os dados estimados
    caminho_csv = f'{e02_dir}dados_estimado_valor_media.csv'
    df = pd.read_csv(caminho_csv, sep=';')

    # Converte a coluna de data para datetime e define como índice
    df['data'] = pd.to_datetime(df['data'])
    df.set_index('data', inplace=True)

    # 2. Identifica a coluna de IBITINGA (primeira após a data)
    col_ibitinga = df.columns[0]

    # Define cores para as demais cidades
    cores = ['red', 'green', 'orange', 'purple']  # Personalizável

    # 3. Cria o gráfico
    plt.figure(figsize=(10, 4))

    # Linha de IBITINGA (valores positivos)
    plt.plot(df.index, df[col_ibitinga], label='IBITINGA', color='blue', linewidth=2)

    # Linhas das outras cidades (valores negativos para separar visualmente)
    for i, coluna in enumerate(df.columns[1:]):
        cor = cores[i % len(cores)]
        nome_cidade = coluna.replace('dados_', '').replace('.csv', '')
        plt.plot(df.index, -df[coluna], label=nome_cidade, color=cor)

    # Linha de referência no zero
    plt.axhline(0, color='black', linewidth=1)

    # Estilização do gráfico
    plt.title('IBITINGA (acima) vs Outras Cidades (abaixo)')
    plt.xlabel('Data')
    plt.ylabel('Precipitação')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.grid(True)
    plt.tight_layout()

    # 4. Salva o gráfico
    caminho_saida = f'{e02_dir}grafico_analise_e02_a4_horizontal.png'
    plt.savefig(caminho_saida, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Gráfico salvo em: {caminho_saida}")

# Executa a função se o script for rodado diretamente
if __name__ == "__main__":
    gerar_grafico_estimado_ibitinga()
