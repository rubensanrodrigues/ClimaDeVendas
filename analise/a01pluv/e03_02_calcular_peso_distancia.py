import json

def calcular_pesos_por_distancia():
    # Diretório de entrada/saída
    e03_dir = 'e03/'

    # Evita divisão por zero para distâncias muito pequenas
    epsilon = 0.01

    # 1. Lê as distâncias do arquivo JSON
    caminho_distancias = f'{e03_dir}distancias_ibitinga.json'
    with open(caminho_distancias, 'r') as arquivo_json:
        distancias_ibitinga = json.load(arquivo_json)

    # 2. Calcula os pesos brutos (inverso da distância)
    pesos = {}
    for cidade, distancia in distancias_ibitinga.items():
        pesos[cidade] = 1 / (distancia + epsilon)

    # 3. Normaliza os pesos para que a soma seja 1
    soma_pesos = sum(pesos.values())
    pesos_normalizados = {cidade: peso / soma_pesos for cidade, peso in pesos.items()}

    # 4. Salva os pesos normalizados em um arquivo JSON
    caminho_saida = f'{e03_dir}pesos_distancia.json'
    with open(caminho_saida, 'w') as arquivo_json:
        json.dump(pesos_normalizados, arquivo_json, indent=4)

    print(f"Pesos normalizados por distância salvos em: {caminho_saida}")

# Executa a função se o script for chamado diretamente
if __name__ == "__main__":
    calcular_pesos_por_distancia()
