import csv
import json

def calcular_pesos_media_e_distancia():
    e02_dir = 'e02/'
    e03_dir = 'e03/'
    e04_dir = 'e04/'

    # 1. Lê os pesos históricos
    with open(f'{e02_dir}pesos.json', 'r') as arquivo_json:
        pesos_historicos = json.load(arquivo_json)

    # Remove IBITINGA, pois queremos estimá-la
    pesos_historicos.pop('A737_IBITINGA', None)

    # 2. Lê as distâncias entre as estações e IBITINGA
    with open(f'{e03_dir}distancias_ibitinga.json', 'r') as arquivo_json:
        distancias_km = json.load(arquivo_json)

    # 3. Ajusta os pesos históricos pela distância
    pesos_ponderados = {}
    soma_inversos = 0.0

    for estacao in pesos_historicos:
        peso_hist = pesos_historicos[estacao]
        dist = distancias_km[estacao]
        peso_ajustado = peso_hist / dist
        pesos_ponderados[estacao] = peso_ajustado
        soma_inversos += peso_ajustado

    # 4. Normaliza os pesos para que somem 1.0
    for estacao in pesos_ponderados:
        pesos_ponderados[estacao] /= soma_inversos

    # 5. Salva os pesos no JSON
    with open(f'{e04_dir}pesos_media_e_distancia.json', 'w') as arquivo_json:
        json.dump(pesos_ponderados, arquivo_json)

    print(f"Arquivo salvo: {e04_dir}pesos_media_e_distancia.json")

if __name__ == "__main__":
    calcular_pesos_media_e_distancia()
