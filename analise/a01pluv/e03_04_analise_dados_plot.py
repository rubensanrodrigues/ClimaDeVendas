import pandas as pd
import matplotlib.pyplot as plt

def gerar_grafico_estimativa_distancia():
    e03_dir = 'e03/'

    # Lê o CSV
    df = pd.read_csv(f'{e03_dir}dados_estimado_valor_distancia.csv', sep=';')
    df['data'] = pd.to_datetime(df['data'])
    df.set_index('data', inplace=True)

    col_ibitinga = df.columns[0]

    cores = ['red', 'green', 'orange', 'purple']

    plt.figure(figsize=(10, 4))

    # Linha principal (IBITINGA)
    plt.plot(df.index, df[col_ibitinga], label='IBITINGA', color='blue', linewidth=2)

    # Demais estações invertidas
    for i, coluna in enumerate(df.columns[1:]):
        cor = cores[i % len(cores)]
        nome_cidade = coluna.replace('dados_', '').replace('.csv', '')
        plt.plot(df.index, -df[coluna], label=nome_cidade, color=cor)

    plt.axhline(0, color='black', linewidth=1)
    plt.title('IBITINGA (acima) vs Outras Cidades (abaixo)')
    plt.xlabel('Data')
    plt.ylabel('Precipitação')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.grid(True)
    plt.tight_layout()

    # Salvar gráfico seguindo o padrão
    caminho_saida = f'{e03_dir}grafico_analise_e03_a4_horizontal.png'
    plt.savefig(caminho_saida, dpi=300, bbox_inches='tight')
    print(f"Gráfico salvo em: {caminho_saida}")

if __name__ == "__main__":
    gerar_grafico_estimativa_distancia()
