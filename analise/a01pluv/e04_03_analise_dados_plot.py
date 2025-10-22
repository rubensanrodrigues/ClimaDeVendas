import pandas as pd
import matplotlib.pyplot as plt

def plotar_grafico_estimado_med_dist():
    e04_dir = 'e04/'

    # 1. Lê o CSV com os dados estimados
    df = pd.read_csv(f'{e04_dir}dados_estimado_valor_media_e_distancia.csv', sep=';')
    df['data'] = pd.to_datetime(df['data'])
    df.set_index('data', inplace=True)

    # 2. Define a coluna de IBITINGA
    col_ibitinga = df.columns[0]

    # 3. Define as cores das demais cidades
    cores = ['red', 'green', 'orange', 'purple']  # Pode ajustar se necessário

    # 4. Criação do gráfico
    plt.figure(figsize=(10, 4))

    # Linha para IBITINGA (acima do eixo)
    plt.plot(df.index, df[col_ibitinga], label='IBITINGA', color='blue', linewidth=2)

    # Linhas para outras cidades (invertidas, abaixo do eixo)
    for i, coluna in enumerate(df.columns[1:]):
        cor = cores[i % len(cores)]
        nome_cidade = coluna.replace('dados_', '').replace('.csv', '')
        plt.plot(df.index, -df[coluna], label=nome_cidade, color=cor)

    # Linha do zero no eixo Y
    plt.axhline(0, color='black', linewidth=1)

    # 5. Estética do gráfico
    plt.title('IBITINGA (acima) vs Outras Cidades (abaixo)')
    plt.xlabel('Data')
    plt.ylabel('Precipitação')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.grid(True)
    plt.tight_layout()

    # 6. Salva a figura
    nome_arquivo = f'{e04_dir}grafico_analise_e04_a4_horizontal.png'
    plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
    print(f"Gráfico salvo em: {nome_arquivo}")

if __name__ == "__main__":
    plotar_grafico_estimado_med_dist()
