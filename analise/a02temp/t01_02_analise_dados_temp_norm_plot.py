import pandas as pd
import matplotlib.pyplot as plt

t01 = 't01/'

# Lê o CSV
df = pd.read_csv(f'{t01}dados_A737_IBITINGA_TEMP_NORM.csv', sep=';', )
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df.set_index('data', inplace=True)


# Cores para as demais estações
cores = ['red', 'blue', 'green']  # Customize aqui

# Criar o gráfico
plt.figure(figsize=(10, 4))

# Plot das outras estações com cores definidas
for i, coluna in enumerate(df.columns[0:]):
    cor = cores[i % len(cores)]  # Garante que não dá erro se tiver mais estações que cores
    df.columns = df.columns.str.strip()
    plt.plot(df.index, df[coluna], label=coluna, color=cor)

# Linha do zero
plt.axhline(0, color='black', linewidth=1)

# Estética
plt.title('Variação das Temperaturas Máxima, Média e Mínima - Ibitinga')
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.tight_layout()
plt.show()
#plt.savefig(f'{e01_dir}grafico_a4_horizontal.png', dpi=300, bbox_inches='tight')
