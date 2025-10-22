import pandas as pd
import matplotlib.pyplot as plt

def gerar_grafico_meteorologico():
    # Diretório de entrada e saída
    e01_dir = 'e01/'

    # 1. Ler o arquivo CSV gerado anteriormente
    caminho_csv = f'{e01_dir}dados_estmet_join.csv'
    df = pd.read_csv(caminho_csv, sep=';')

    # 2. Preparar os dados
    df['data'] = pd.to_datetime(df['data'])
    df.set_index('data', inplace=True)

    # 3. Identificar coluna de IBITINGA (primeira coluna após a data)
    col_ibitinga = df.columns[0]

    # 4. Definir cores para as demais cidades
    cores = ['red', 'green', 'orange', 'purple']  # Customize se tiver mais cidades

    # 5. Criar gráfico
    plt.figure(figsize=(10, 4))

    # Plotar linha de IBITINGA (com valor positivo)
    plt.plot(df.index, df[col_ibitinga], label='IBITINGA', color='blue', linewidth=2)

    # Plotar demais cidades (valores negativos para separar visualmente)
    for i, coluna in enumerate(df.columns[1:]):
        cor = cores[i % len(cores)]  # Evita erro se tiver mais cidades do que cores
        nome_cidade = coluna.replace('dados_', '').replace('.csv', '')
        plt.plot(df.index, -df[coluna], label=nome_cidade, color=cor)

    # Linha do zero no meio
    plt.axhline(0, color='black', linewidth=1)

    # Estilizar o gráfico
    plt.title('IBITINGA (acima) vs Outras Cidades (abaixo)')
    plt.xlabel('Data')
    plt.ylabel('Precipitação')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.grid(True)
    plt.tight_layout()

    # 6. Salvar o gráfico
    caminho_saida = f'{e01_dir}grafico_analise_e01_a4_horizontal.png'
    plt.savefig(caminho_saida, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Gráfico salvo em: {caminho_saida}")

# Executa se chamado diretamente
if __name__ == "__main__":
    gerar_grafico_meteorologico()
